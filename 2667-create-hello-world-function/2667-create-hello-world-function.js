/**
 * @return {Function}
 */
var createHelloWorld = function() {
    var char = "Hello World";
    return function(...args) {
        return char;
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */