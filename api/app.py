from flask import Flask, request, url_for, jsonify
from models.models import *
import mongoengine
from resources.routes import routes

app = Flask(__name__)

mongoengine.connect("lijamachankura")

@app.route('/')
def index():
    return "Everything is okay", 200

# -- USER API -- #
@app.route("/api/v1/users/new", methods=["POST"])
def add_user():
    body = request.get_json()
    user = User(**body)
    user.save()
    return user.to_json()


@app.route("/api/v1/users/update/<uid>", methods=["PUT"])
def update_user(uid):
    body = request.get_json()

    old_user = User.objects(id=uid).first()
    old_user = User(**body)
    updated_user = old_user.update().to_json()

    return updated_user


@app.route("/api/v1/users/delete/<cell>", methods=["DELETE"])
def delete_user(cell):
    body = request.get_json()
    user = User.objects(cell_phone=cell).delete()
    return {"message":"User deleted successfully"}, 200


@app.route("/api/v1/users")
def get_users():
    users = User.objects.to_json()
    return users


@app.route("/api/v1/users/<uid>")
def get_user(uid):
    users = User.objects(cell_phone=uid).to_json()
    return users
# -- END OF USER API -- #


# -- CUSTOMER API -- #

# Create an account
@app.route("/api/v1/customers/new", methods=["POST"])
def create_customer_account():
   body = request.get_json()

   print(body)
   
   new_customer = Customer(**body)
   Customer
     
   result = new_customer.save()

   return jsonify({"message":"Customer added successfully","new_customer":result.to_json()})

   # Create an account
@app.route("/api/v1/customers/update/<uid>", methods=["PUT"])
def update_customer_account(uid):
   body = request.get_json()
   
   old_customer = Customer.objects(id=uid).first()
   new_customer = old_customer.update(**body)

   result = new_customer
   return jsonify({"message":"Customer updated successfully","new_customer":result})



# Get all customers
@app.route("/api/v1/customers")
def get_customers():
    customers = Customer.objects.to_json()
    return customers


# Login

# Create a loan request
@app.route("/api/v1/loans/new", methods=['POST'])
def create_loan_request():
    body = request.get_json()
    customer_id = body["customer_id"]
    agent_id = body["agent_id"]
    interest = body["interest"]
    total = body["total_borrowing"]
    approval_status = body["approval_status"]
    
    _customer = Customer.objects(id=customer_id).first()
    _agent = User.objects(id=agent_id).first()

    

    customer = _customer.to_json()
    agent = User()

    loan = Loan()
    loan.customer(customer)
    loan.agent(agent)
    loan.interest(interest)
    loan.total_borrowing(total)
    loan.approval_status(approval_status)
    result = loan.save()
    return loan.to_json()

@app.route("/api/v1/loans")
def get_loans():
    loans = Loan.objects.to_json()
    return loans
    #loan = Loan(**body)

# -- Customer id
# -- Loan amount
# -- Required date
# -- Maturity date

# View loan request status
# Loan airtime
# loan data

# -- END OF CUSTOMER API -- #

if __name__ == "__main__":
    app.run(debug=True)
    
