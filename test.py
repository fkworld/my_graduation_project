import server_start
import flask


def main():
    a = flask.url_for('static',filename='example.css')
    print(a)


if __name__ == '__main__':
    main()
