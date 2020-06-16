from flaskblog import create_app
from flask_script import Manager, Server
from flask_migrate import MigrateCommand

app = create_app()
#manager = Manager(app)

#manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    #manager.run()
    app.run(debug=True)