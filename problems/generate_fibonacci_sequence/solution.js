/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    let first = 0;
    let second = 1

    while (true) {
        yield first;
        third = first + second;
        first = second;
        second = third;
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */