from flask import Blueprint, render_template, request, redirect

from pos.models import db
from pos.models.transaction import Transactions
from pos.models.transaction_products import TransactionProducts

bp = Blueprint("transaction", __name__)


@bp.route("/transaction")
def transaction_list():
    """List transaction"""
    transactions = Transactions.query.all()
    return render_template("transaction/list.html", transactions=transactions)


@bp.route("/transaction/add", methods=["POST", "GET"])
def transaction_all():
    """Add new transaction"""
    if request.method == "GET":
        return render_template("transaction/form_add.html")

    products = request.form.getlist('products')
    products_qty = request.form.getlist('products_qty')

    transaction = Transactions()
    db.session.add(transaction)
    db.session.flush()

    for key, product in enumerate(products):
        transaction_product = TransactionProducts()
        transaction_product.transaction_id = transaction.id
        transaction_product.product_id = int(product)
        transaction_product.product_qty = int(products_qty[key])
        db.session.add(transaction_product)
        db.session.flush()

    db.session.commit()

    return redirect("/transaction")

