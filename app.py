import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_collections")
def get_collections():
    collections = list(mongo.db.meal_types.find())
    categories = list(mongo.db.categories.find())
    return render_template(
        "home_page.html", collections=collections, categories=categories)


@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
    return render_template("recipes.html", recipes=recipes)


@app.route("/get_age_groups")
def get_age_groups():
    categories = list(mongo.db.categories.find())
    return render_template(
        "age_groups.html", categories=categories)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


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
    # get the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("account.html", username=username)

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
            "age_group": request.form.get("age_group")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "age_group": request.form.get("age_group")
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


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
