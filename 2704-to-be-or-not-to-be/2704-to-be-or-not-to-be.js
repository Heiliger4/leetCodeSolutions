var expect = function(val1) {
    return {
        toBe: (val2) => (val1 === val2) ? true : (() => { throw new Error("Not Equal"); })(),
        notToBe: (val2) => (val1 !== val2) ? true : (() => { throw new Error("Equal"); })()
    };
};

try {
    console.log(expect(5).toBe(5));  // true
} catch (e) {
    console.error(e.message);
}

try {
    expect(5).notToBe(5);  // Throws "Equal"
} catch (e) {
    console.error(e.message);  // Logs: "Equal"
}

try {
    console.log(expect(5).notToBe(6));  // true
} catch (e) {
    console.error(e.message);
}
