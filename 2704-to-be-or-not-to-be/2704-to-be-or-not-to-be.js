var expect = function(val1) {
    return {
        toBe: (val2) => (val1 === val2) ? true : (() => { throw new Error("Not Equal"); })(),
        notToBe: (val2) => (val1 !== val2) ? true : (() => { throw new Error("Equal"); })()
    };
};


console.log(expect(5).toBe(5)); 
try {
    expect(5).notToBe(5); 
} catch (e) {
    console.error(e.message); 
}


func = () => expect(5).toBe(5)



expect(5).toBe(5); // true
expect(5).notToBe(5); // throws "Equal"
