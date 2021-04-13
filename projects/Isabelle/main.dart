import 'dart:html';
import 'dart:collection';
import 'dart:async';
import 'dart:math';

const int CELL_SIZE = 10;

CanvasElement canvas;
CanvasRenderingContext2D ctx;

Keyboard keyboard = new Keyboard();

void main() {
    canvas = querySelector('#canvas')..focus();
    ctx = canvas.getContext('2d');

    new Game()..run();
}

void drawCell(Point coords, String color) {
    ctx..fillStyle = color..strokeStyle = "white";

    final int x = coords.x * CELL_SIZE;
    final int y = coords.y * CELL_SIZE;
//Drawing the filled rectangle and border
    ctx..fillRect(x, y, CELL_SIZE, CELL_SIZE)..strokeRect(x, y, CELL_SIZE, CELL_SIZE);
}
//Reset the board
void clear() {
    ctx..fillStyle = "white"..fillRect(0, 0, canvas.width, canvas.height);

}
//This method listens to KeyDown and KeyUp events from the browser. It keeps track of 
//which keys are pressed.
class Keyboard {
    HashMap < int, num > _keys = new HashMap < int, num > ();

    Keyboard() {
        window.onKeyDown.listen((KeyboardEvent event) {
            _keys.putIfAbsent(event.keyCode, () => event.timeStamp);
        });

        window.onKeyUp.listen((KeyboardEvent event) {
            _keys.remove(event.keyCode);
        });
    }

    bool isPressed(int keyCode) => _keys.containsKey(keyCode);
}

class Snake {
    static
    const Point LEFT =
        const Point(-1, 0);
    static
    const Point RIGHT =
        const Point(1, 0);
    static
    const Point UP =
        const Point(0, -1);
    static
    const Point DOWN =
        const Point(0, 1);
    static
    const int START_LENGTH = 5;

    List < Point > _body;

    Point _dir = RIGHT;

    Snake() {
        int i = START_LENGTH - 1;
        _body = new List < Point > .generate(START_LENGTH, (int index) => new Point(i--, 0));
    }

    Point get head => _body.first;
    
    void _checkInput() {
        if (keyboard.isPressed(KeyCode.LEFT) && _dir != RIGHT) {
            _dir = LEFT;
        } else if (keyboard.isPressed(KeyCode.RIGHT) && _dir != LEFT) {
            _dir = RIGHT;
        } else if (keyboard.isPressed(KeyCode.UP) && _dir != DOWN) {
            _dir = UP;
        } else if (keyboard.isPressed(KeyCode.DOWN) && _dir != UP) {
            _dir = DOWN;
        }
    }

    void grow() {
        //Adding a head 
        _body.insert(0, head + _dir);
    }

    void _move() {
        //Make the snake move by adding to the head and removing from tail
        grow();
        _body.removeLast();
    }

    void _draw() {
        for (Point p in _body) {
            drawCell(p, "pink");
        }
    }

    bool checkForBodyCollision() {
        for (Point p in _body.skip(1)) {
            if (p == head) {
                return true;
            }
        }
        return false;
    }

    void update() {
        _checkInput();
        _move();
        _draw();
    }
}

Point snakeHead =
    const Point(5, 5);
Point moveRight =
    const Point(1, 0);

Point newSnakeHead = snakeHead + moveRight;

class Game {
    static
    const GAME_SPEED = 50;
    num _lastTimeStamp = 0;

    int _rightEdgeX;
    int _bottomEdgeY;

    Snake _snake;
    Point _food;

    Game() {
        _rightEdgeX = canvas.width~/ CELL_SIZE;
        _bottomEdgeY = canvas.height~/ CELL_SIZE;

        init();
    }
    void init() {
        _snake = new Snake();
        _food = _randomPoint();
    }

    Point _randomPoint() {
        Random random = new Random();
        return new Point(random.nextInt(_rightEdgeX), random.nextInt(_bottomEdgeY));
    }

    void _checkForCollisions() {
       //If the snake runs into food
        if (_snake.head == _food) {
            _snake.grow();
            _food = _randomPoint();
        }

        //If the snake needs to be reset
        if (_snake.head.x <= -1 ||
            _snake.head.x >= _rightEdgeX ||
            _snake.head.y <= -1 ||
            _snake.head.y >= _bottomEdgeY ||
            _snake.checkForBodyCollision()) {
            init();
        }
    }
    Future run() async {
        update(await window.animationFrame);
    }

    void update(num delta) {
        final num diff = delta - _lastTimeStamp;

        if (diff > GAME_SPEED) {
            _lastTimeStamp = delta;
            clear();
            drawCell(_food, "red");
            _snake.update();
            _checkForCollisions();
        }

        // keep looping
        run();
    }
}