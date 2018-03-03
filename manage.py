# manage.py
import unittest
from flask_script import Manager
from project import create_app, db
from project.api.models import User
import coverage

app = create_app()
manager = Manager(app)

COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'project/tests/*'
    ]
)
COV.start()
//2汉文化jf
@manager.command
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover('project/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    return 1

@manager.command
def seed_db():
    """Seeds the database."""
    db.session.add(User(username='cnych', email="qikqiak@gmail.com"))
    db.session.add(User(username='chyang', email="icnych@gmail.com"))
    db.session.commit()

@manager.command
def recreate_db():
    """重新创建数据表."""
    db.drop_all()
    db.create_all()
    db.session.commit()

@manager.command
def test():
    """运行测试."""
    tests = unittest.TestLoader().discover('project/tests', pattern='test_*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
