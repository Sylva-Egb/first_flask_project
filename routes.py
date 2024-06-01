from flask import Blueprint, redirect, render_template, request, flash
from models import Todo,db

def init_routes(app):
    from forms import TodoForm
    main_bp = Blueprint('main', __name__)
    @main_bp.route('/', methods=['POST', 'GET'])
    def index():
        form = TodoForm()
        if request.method == 'POST':
            if form.validate_on_submit():
                task = Todo(content=form.content.data)

                try:
                    db.session.add(task)
                    db.session.commit()
                    flash("Task successfully added", "success")

                    return redirect('/')
                except Exception as e:
                    db.session.rollback()
                    flash("Error while adding task: "+ str(e), 'danger')
                    redirect('/')
            else:
                flash("Form validation failed", "danger")

        tasks = Todo.query.order_by(Todo.created_at).all()
        return render_template('index.html', tasks=tasks, form=form)

    @main_bp.route("/delete/<int:id>")
    
    def delete(id):
        task = Todo.query.get_or_404(id)

        try:
            db.session.delete(task)
            db.session.commit()
            flash("Task successfully deleted", "success")
            return redirect('/')
        except Exception as e:
            db.session.rollback()
            flash("Error while deleting task: "+ str(e), 'danger')
            redirect('/')
        
    @main_bp.route("/update/<int:id>", methods=['GET', 'POST'])
    def update(id):
        task = Todo.query.get_or_404(id)
        form = TodoForm(obj=task)
        if request.method == 'POST':
            if form.validate_on_submit():
                task.content = form.content.data
                try:
                    db.session.commit()
                    flash("Task successfully updated", "success")
                    return redirect('/')
                except Exception as e:
                    db.session.rollback()
                    flash("Error while updating task: " + str(e), 'danger')
                    return redirect('/')
        return render_template('update.html', form=form, task=task)

    app.register_blueprint(main_bp)