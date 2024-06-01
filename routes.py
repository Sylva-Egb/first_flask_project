from flask import Blueprint, redirect, render_template, request
from models import Todo,db

def init_routes(app):
    main_bp = Blueprint('main', __name__)
    @main_bp.route('/', methods=['POST', 'GET'])
    def index():
        if request.method == 'POST':
            task_content = request.form['content']
            task = Todo(content= task_content)

            try:
                db.session.add(task)
                db.session.commit()
                return redirect('/')
            except Exception as e:
                return 'Error' + e
            
        else:
            tasks = Todo.query.order_by(Todo.created_at).all()

            return render_template('index.html', tasks = tasks)
    @main_bp.route("/delete/<int:id>")
    
    def delete(id):
        task = Todo.query.get_or_404(id)

        try:
            db.session.delete(task)
            db.session.commit()
            return redirect('/')
        except:
            return "Something went wrong while deleting"

    @main_bp.route("/update/<int:id>", methods=['GET','POST'])
    def update(id):
        task = Todo.query.get_or_404(id)
        if request.method== 'POST':

            task.content = request.form['content']

            try:
                db.session.commit()
                return redirect('/')
            except:
                return 'Something went wrong while updating'

        else:
            return render_template('update.html', task=task)
    app.register_blueprint(main_bp)