import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.json_util import dumps, loads
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    return get_collections()


@app.route("/get_collections")
def get_collections():
    collections = list(mongo.db.meal_types.find())
    categories = list(mongo.db.categories.find())
    unique_categories = list(mongo.db.unique_categories.find())

    return render_template(
        "home_page.html",
        collections=collections,
        categories=categories,
        unique_categories=unique_categories)


@app.route("/get_recipes")
def get_recipes():
    __request_default_route()

    recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
    # code borrowed from
    # https://www.reddit.com/r/flask/comments/25zjtb/af_can_someone_show_me_how_to_build_json_object/
    json_data = dumps(recipes, )

    return render_template(
        "recipes.html",
        recipes=recipes,
        page_title="All recipes",
        json_data=json_data)


@app.route("/category_recipes/<category_name>")
def category_recipes(category_name):
    __request_default_route()

    in_meal_type = mongo.db.meal_types.find({"meal_type": str(category_name)})

    if in_meal_type and in_meal_type.count() > 0:
        recipes = list(
            mongo.db.recipes.find({"meal_type": str(category_name)}))
        json_data = dumps(recipes, )

        return render_template(
            "recipes.html",
            recipes=recipes,
            page_title="{} {}".format("Meal type:", str(category_name)),
            json_data=json_data
            )

    in_category = mongo.db.categories.find({"age_group": str(category_name)})

    if in_category and in_category.count() > 0:
        recipes = list(
            mongo.db.recipes.find({"age_group": str(category_name)}))
        json_data = dumps(recipes, )

        return render_template(
            "recipes.html",
            recipes=recipes,
            page_title="{} {}".format("Age group:", str(category_name)),
            json_data=json_data
            )

    in_unique = mongo.db.unique_categories.find_one(
        {"name": str(category_name)})

    if in_unique and len(in_unique) > 0:
        print("In uniques")

        if in_unique["name"] == "Super quick recipes":
            recipes = list(
                mongo.db.recipes.find(
                    {"cooking_time": "Less than 10 minutes"}))
            json_data = dumps(recipes, )

            return render_template(
                "recipes.html",
                recipes=recipes,
                page_title="{} - {}".format(
                    in_unique["name"], in_unique["description"]),
                json_data=json_data
            )

        if in_unique["name"] == "Quick recipes":
            less_10_minutes_recipes = list(
                mongo.db.recipes.find(
                    {"cooking_time": "Less than 10 minutes"}))
            recipes = list(
                mongo.db.recipes.find(
                    {"cooking_time": "10-20 minutes"}))
            result_recipes = less_10_minutes_recipes + recipes
            json_data = dumps(result_recipes, )

            return render_template(
                "recipes.html",
                recipes=result_recipes,
                page_title="{} - {}".format(
                    in_unique["name"], in_unique["description"]),
                json_data=json_data
            )

        status = "other"

        def generic_render(status: str, page_title: str):
            favorite_recipes = __form_status_favorite_recipes(status)
            json_data = dumps(favorite_recipes, )
            return render_template(
                "recipes.html",
                recipes=favorite_recipes,
                page_title=page_title,
                json_data=json_data)

        if in_unique["name"] == "Grandfather's favourites":
            status = "grandfather"
            return generic_render(status, in_unique["name"])
        elif in_unique["name"] == "Grandmas' favourites":
            status = "grandmother"
            return generic_render(status, in_unique["name"])
        elif in_unique["name"] == "Moms' favourites":
            status = "mother"
            return generic_render(status, in_unique["name"])
        elif in_unique["name"] == "Dads' favourites":
            status = "father"
            return generic_render(status, in_unique["name"])
        elif in_unique["name"] == "other":
            return generic_render(status, in_unique["name"])

    return render_template(
        "recipes.html",
        recipes=[],
        page_title="Fail",
        json_data=dumps([]))


def __form_status_favorite_recipes(status: str) -> list:
    all_status_users = list(mongo.db.users.find({"status": status}))
    all_ids = [item['_id'] for item in all_status_users]  # get list ObjectId

    if len(all_ids) > 0:
        all_favorite_recipes = []

        for item in all_ids:
            foo = mongo.db.user_favorite_recipes.find_one(
                {"user_id": ObjectId(item)})
            if foo:
                all_favorite_recipes += foo["recipes_id"]

        all_favorite_recipes = set(all_favorite_recipes)  # only unique items
        all_favorite_recipes = [ObjectId(it) for it in all_favorite_recipes]

        all_favorite_recipes = list(
            mongo.db.recipes.find(
                {"_id": {"$in": all_favorite_recipes}}))
        return all_favorite_recipes
    return []


@app.route("/get_age_groups")
def get_age_groups():
    categories = list(mongo.db.categories.find())
    return render_template(
        "age_groups.html", categories=categories)


@app.route("/search", methods=["GET", "POST"])
def search():
    __request_default_route()

    json_data = request.form.get('json_data')
    query = request.form.get('query')
    title_to_pass = request.form.get('title_to_pass')

    json_data = loads(json_data)  # convert from json-string into json-object
    json_to_pass_data = dumps(json_data)  # passed to template

    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))

    search_result = []
    allowed_ids = [item["_id"] for item in json_data]

    for recipe in recipes:
        if recipe["_id"] in allowed_ids:
            search_result.append(recipe)
    if "Search in:" not in title_to_pass:
        page_title = "Search in: {}".format(title_to_pass)
    else:
        page_title = title_to_pass
    return render_template(
        "recipes.html",
        recipes=search_result,
        page_title=page_title,
        json_data=json_to_pass_data
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email").lower(),
            "status": request.form.get("status").lower()
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("account", username=session["user"]))

    statuses = mongo.db.statuses.find()
    return render_template("register.html", statuses=statuses)


@app.route("/signIn", methods=["GET", "POST"])
def signIn():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"$or": [
                {"username": request.form.get("login").lower()},
                {"email": request.form.get("login").lower()}]}
        )

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = existing_user['username']
                flash("Welcome, {}".format(
                    session["user"]))
                return redirect(url_for(
                    "get_collections", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("signIn"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("signIn"))

    return render_template("signIn.html")


@app.route("/account/<username>", methods=["GET", "POST"])
def account(username):
    __request_default_route()

    # get the session user's username from db
    record = mongo.db.users.find_one(
        {"username": session["user"]})
    username = record["username"]
    user_id = record["_id"]
    if session["user"]:
        recipes = []

        favorites = mongo.db.user_favorite_recipes.find_one(
            {"user_id": user_id})
        if favorites:
            favorite_id = favorites['recipes_id']

            for recipe_id in favorite_id:
                record_recipe = mongo.db.recipes.find_one(
                    {"_id": ObjectId(recipe_id)})

                if record_recipe:
                    print(record_recipe)
                    recipes.append(record_recipe)

        return render_template(
            "account.html",
            username=username,
            favorite_recipes=recipes)

    return redirect(url_for("signIn"))


@app.route("/signOut")
def signOut():
    # remove user from session cookie
    flash("You have been signed out")
    session.pop("user")
    return redirect(url_for("signIn"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        HSE_approved = "on" if request.form.get("HSE_approved") else "off"
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "age_group": request.form.get("age_group"),
            "meal_type": request.form.get("meal_type"),
            "ingredients": request.form.get("ingredients"),
            "cooking_instructions": request.form.get("cooking_instructions"),
            "HSE_approved": HSE_approved,
            "cooking_time": request.form.get("cooking_time"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find()
    meal_types = mongo.db.meal_types.find()
    cooking_time = mongo.db.cooking_time.find()
    return render_template(
        "add_recipe.html", categories=categories, meal_types=meal_types,
        cooking_time=cooking_time)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        HSE_approved = "on" if request.form.get("HSE_approved") else "off"
        submit = {
            "recipe_name": request.form.get("recipe_name"),
            "age_group": request.form.get("age_group"),
            "meal_type": request.form.get("meal_type"),
            "ingredients": request.form.get("ingredients"),
            "cooking_instructions": request.form.get("cooking_instructions"),
            "HSE_approved": HSE_approved,
            "cooking_time": request.form.get("cooking_time"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated")
        return redirect(url_for("get_recipes"))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find()
    meal_types = mongo.db.meal_types.find()
    cooking_time = mongo.db.cooking_time.find()
    return render_template(
        "edit_recipe.html",
        recipe=recipe,
        categories=categories,
        meal_types=meal_types,
        cooking_time=cooking_time)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Deleted")
    return redirect(url_for("get_recipes"))


@app.route("/save_recipe/<recipe_id>", methods=["GET", "POST"])
def save_recipe(recipe_id):
    if "user" in session:
        flash("Recipe successfully added to Your Favourites!")
        return redirect(url_for("get_recipes"))

    else:
        flash("Please sign in to save recipes to your collection")
        return render_template("signIn.html")


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find())
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "age_group": request.form.get("age_group"),
            "description": request.form.get("description")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "age_group": request.form.get("age_group"),
            "description": request.form.get("description")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


@app.route("/add_to_favorite")
def add_to_favorite():
    recipe_id = request.args.get("recipe_id", None)
    username = request.args.get("user_id", None)

    user_id = mongo.db.users.find_one({"username": username})['_id']

    existing_record = mongo.db.user_favorite_recipes.find_one(
        {"user_id": user_id})
    if existing_record:
        if recipe_id not in existing_record['recipes_id']:
            lst = list(existing_record['recipes_id'])
            lst.append(recipe_id)
            mongo.db.user_favorite_recipes.update_one(
                {"user_id": user_id},
                {"$set": {"recipes_id": lst}}
            )
    else:
        mongo.db.user_favorite_recipes.insert_one(
            {"user_id": user_id, "recipes_id": [recipe_id]}
        )

    return redirect(url_for("account", username=username))


@app.route("/remove_from_favorite")
def remove_from_favorite():
    recipe_id = request.args.get("recipe_id", None)
    username = request.args.get("user_id", None)

    user_id = mongo.db.users.find_one({"username": username})['_id']

    existing_record = mongo.db.user_favorite_recipes.find_one(
        {"user_id": user_id})
    favorite_list = [
        item for item in existing_record["recipes_id"] if item != recipe_id]

    mongo.db.user_favorite_recipes.update_one(
        {"user_id": user_id},
        {"$set": {"recipes_id": favorite_list}}
    )

    return redirect(url_for("account", username=username))


@app.route("/_add_view_on_recipe")
def _add_view_on_recipe():
    id_recipe = request.args.get("id_recipe")
    views_recipe = 0

    recipe = list(mongo.db.recipes.find({"_id": ObjectId(id_recipe)}))

    if recipe and len(recipe) > 0:

        if "views" in recipe[-1]:
            views_recipe = recipe[-1]["views"]

        mongo.db.recipes.update_one(
            {"_id": ObjectId(id_recipe)},
            {"$set": {"views": views_recipe+1}}
        )
    print("#### Add view on recipe")
    print(views_recipe)
    from flask import jsonify
    return jsonify(views=views_recipe)


def __request_default_route():
    pass


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
