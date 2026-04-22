import assert from "assert";
import { mostFrequent, formatNames } from "./interview_practice";

let passed = 0;
let failed = 0;

function test(description: string, actual: string, expected: string) {
    if (actual === expected) {
        console.log(`  ✓ ${description}`);
        passed++;
    } else {
        console.log(`  ✗ ${description}`);
        console.log(`    expected: "${expected}", got: "${actual}"`);
        failed++;
    }
}

console.log("mostFrequent");

test(
    "returns the most frequent item",
    mostFrequent(["apple", "banana", "apple", "cherry", "banana", "apple"]),
    "apple"
);

test(
    "single item array",
    mostFrequent(["only"]),
    "only"
);

// test(
//     "one",
//     formatNames(["John Smith", "Ada Lovelace", "Grace Hopper"]),
//     ["Hopper, Grace", "Lovelace, Ada", "Smith, John"]
// );
console.log(`\n${passed} passed, ${failed} failed`);
