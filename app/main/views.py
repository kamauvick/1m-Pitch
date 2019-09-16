from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from . import main
from ..models import Post, Comment


@main.route('/')
def index():
    posts = Post.query.all()
    pickup = Post.query.filter_by(category='Pickup_lines').all()
    product = Post.query.filter_by(category='Product').all()
    idea = Post.query.filter_by(category='Idea').all()

    return render_template('index.html', pickup=pickup, product=product, idea=idea)


@main.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST':
        form = request.form
        title = form.get('title')
        post = form.get('post')
        category = form.get('category')
        user_id = current_user
        post_obj = Post(post=post, title=title, category=category, user_id=current_user._get_current_object().id)
        post_obj.save()
        return redirect(url_for('/'))
    return render_template('pitch.html')


@main.route('/comment/<int:post_id>', methods=['GET', 'POST'])
@login_required
def comment(post_id):
    if request.method == 'POST':
        form = request.form
        # Post = Post.query.get(post_id)
        comments = Comment.query.filter_by(post_id=post_id).all()
        comment = form.get('comment')
        post_id = post_id
        new_comment = Comment(
            user_id=current_user.id,
            post_id=str(request.form.get('post_id')),
            comment=str(request.form.get('comment'))
        )
        new_comment.save()
        new_comments = [new_comment]
        print(new_comments)
        return url_for('.comment', post_id= post_id)
    return render_template('comment.html')
