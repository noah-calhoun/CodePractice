// Interview Practice — Foundations + Real World (TypeScript)
// Work through one problem at a time. Talk through your thinking out loud.
// Run with: npx ts-node src/interview_practice.ts
// ─────────────────────────────────────────────────────────────────────────────


// ── PROBLEM 1 ─────────────────────────────────────────────────────────────────
// Most Frequent Item
//
// Given an array of strings, return the one that appears most often.
// If there's a tie, return any one of them.
//
// Example:
//   mostFrequent(["apple", "banana", "apple", "cherry", "banana", "apple"])
//   → "apple"

export function mostFrequent(items: string[]): string {
    const counts = new Map<string, number>()
    for (const item of items) {
        counts.set(item, (counts.get(item) ?? 0) + 1)
    }
    const maxVal = Math.max(...counts.values());
    for (const [key, value] of counts) {
        if (value === maxVal) return key
    }
    return ""

    // OLD:
    // const itemDict = new Map()
    // for (const item of items){
    //     const count = itemDict.get(item)
    //     if (count){
    //         itemDict.set(item, count + 1)
    //     }
    //     else{
    //         itemDict.set(item, 1)
    //     }
    // }
    // const maxVal: number = Math.max(...itemDict.values());
    // for (const [key, val] of itemDict){
    //     if (val === maxVal) return key
    // }
    // return ""
}


// ── PROBLEM 2 ─────────────────────────────────────────────────────────────────
// Name Formatter
//
// Given an array of names in "First Last" format, return them reformatted as
// "Last, First" and sorted alphabetically by last name.
//
// Example:
//   formatNames(["John Smith", "Ada Lovelace", "Grace Hopper"])
//   → ["Hopper, Grace", "Lovelace, Ada", "Smith, John"]

export function formatNames(names: string[]): string[] {
    const flipped: string[] = []
    // flip names first
    for (const i in names) {
        const name = names[i].split(" ")
        flipped.push(`${name[1]}, ${name[0]}`)
    }
    flipped.sort()
    // sort based off first few characters

    return flipped;
}


// ── PROBLEM 3 ─────────────────────────────────────────────────────────────────
// Total Spend Per User
//
// You're given an array of transaction objects, each with a "user" and "amount".
// Return an object mapping each user to their total spend,
// sorted by total (highest first).
//
// Example:
//   const txns = [
//     { user: "alice", amount: 50 },
//     { user: "bob",   amount: 30 },
//     { user: "alice", amount: 20 },
//   ]
//   totalSpend(txns) → { alice: 70, bob: 30 }

interface Transaction {
    user: string;
    amount: number;
}

function totalSpend(transactions: Transaction[]): Record<string, number> {
    const output = new Map<string, number>()
    for (const item of transactions) {
        output.set(item.user, (output.get(item.user) ?? 0) + item.amount)
    }

    return Object.fromEntries([...output].sort((a, b) => b[1] - a[1]))
}


// ── PROBLEM 4 ─────────────────────────────────────────────────────────────────
// Parse Server Logs
//
// You're given an array of log lines, each in this format:
//   "YYYY-MM-DD username ACTION"
//
// Return an object mapping each username to the list of actions they performed,
// in the order they appear in the log.
//
// Example:
//   const logs = [
//     "2024-01-10 alice LOGIN",
//     "2024-01-10 bob LOGIN",
//     "2024-01-11 alice UPLOAD",
//     "2024-01-11 alice LOGOUT",
//   ]
//   parseLogs(logs) → {
//     alice: ["LOGIN", "UPLOAD", "LOGOUT"],
//     bob:   ["LOGIN"]
//   }

function parseLogs(logs: string[]): Record<string, string[]> {
    const people = new Map()
    // create map of people names first, then append their action
    for (const i in logs) {
        // check if person present, add if not
        const parsed = logs[i].split(" ")
        const name = parsed[1]
        const action = parsed[2]
        if (!name || !action) {
            continue
        }
        people.get(name) ?? people.set(name, [])
        people.get(name).push(action)


    }
    return Object.fromEntries(people);
}


// ── PROBLEM 5 ─────────────────────────────────────────────────────────────────
// Shopping Cart
//
// Implement a ShoppingCart class that supports:
//   addItem(name, price)  — add an item with its price
//   removeItem(name)      — remove an item by name (do nothing if not found)
//   getTotal()            — return the sum of all item prices
//   getItems()            — return the array of item names currently in the cart
//
// Example:
//   const cart = new ShoppingCart()
//   cart.addItem("shirt", 29.99)
//   cart.addItem("jeans", 59.99)
//   cart.removeItem("shirt")
//   cart.getTotal()   → 59.99
//   cart.getItems()   → ["jeans"]

class ShoppingCart {
    private items = new Map<string, number>()

    addItem(name: string, price: number): void {
        this.items.set(name, price)
    }


    removeItem(name: string): void {
        this.items.delete(name)
    }

    getTotal(): number {
        let total = 0
        for (const [name, price] of this.items) {
            total += price
        }
        return total;
    }

    getItems(): string[] {
        return [...this.items.keys()];
    }
}


// ── PROBLEM 6 ─────────────────────────────────────────────────────────────────
// Top Earners by Department
//
// Given an array of employee objects (each with "name", "department", "salary"),
// return an object mapping each department to the name of its highest-paid employee.
//
// Example:
//   const employees = [
//     { name: "Alice", department: "Engineering", salary: 95000 },
//     { name: "Bob",   department: "Engineering", salary: 88000 },
//     { name: "Carol", department: "Marketing",   salary: 72000 },
//     { name: "Dave",  department: "Marketing",   salary: 75000 },
//   ]
//   topEarners(employees) → { Engineering: "Alice", Marketing: "Dave" }

interface Employee {
    name: string;
    department: string;
    salary: number;
}

function topEarners(employees: Employee[]): Record<string, string> {
    return {};
}


// ─────────────────────────────────────────────────────────────────────────────

// Problem 1
console.log("── Problem 1 ──");
console.log(mostFrequent(["apple", "banana", "apple", "cherry", "banana", "apple"]));
// Expected: "apple"

// Problem 2
console.log("\n── Problem 2 ──");
console.log(formatNames(["John Smith", "Ada Lovelace", "Grace Hopper"]));
// Expected: ["Hopper, Grace", "Lovelace, Ada", "Smith, John"]

// Problem 3
console.log("\n── Problem 3 ──");
const txns: Transaction[] = [
    { user: "alice", amount: 50 },
    { user: "bob", amount: 30 },
    { user: "alice", amount: 20 },
    { user: "bob", amount: 90 },
];
console.log(totalSpend(txns));
// Expected: { bob: 120, alice: 70 }

// Problem 4
console.log("\n── Problem 4 ──");
const logs = [
    "2024-01-10 alice LOGIN",
    "2024-01-10 bob LOGIN",
    "2024-01-11 alice UPLOAD",
    "2024-01-11 alice LOGOUT",
];
console.log(parseLogs(logs));
// Expected: { alice: ["LOGIN", "UPLOAD", "LOGOUT"], bob: ["LOGIN"] }

// Problem 5
console.log("\n── Problem 5 ──");
const cart = new ShoppingCart();
cart.addItem("shirt", 29.99);
cart.addItem("jeans", 59.99);
cart.addItem("hat", 15.00);
cart.removeItem("shirt");
console.log(cart.getTotal());   // 74.99
console.log(cart.getItems());   // ["jeans", "hat"]

// Problem 6
console.log("\n── Problem 6 ──");
const employees: Employee[] = [
    { name: "Alice", department: "Engineering", salary: 95000 },
    { name: "Bob", department: "Engineering", salary: 88000 },
    { name: "Carol", department: "Marketing", salary: 72000 },
    { name: "Dave", department: "Marketing", salary: 75000 },
];
console.log(topEarners(employees));
// Expected: { Engineering: "Alice", Marketing: "Dave" }


console.log(formatNames(["John Smith", "Ada Lovelace", "Grace Hopper"]));
console.log(totalSpend([
    { user: "alice", amount: 50 },
    { user: "bob", amount: 30 },
    { user: "alice", amount: 20 },
]));
console.log(parseLogs([
    "2024-01-10 alice LOGIN",
    "2024-01-10 bob LOGIN",
    "2024-01-11 alice UPLOAD",
    "2024-01-11 alice LOGOUT",
]))
console.log(formatNames(["John Smith", "Ada Lovelace", "Grace Hopper"]));



// For this problem, we're going to work with call event data. This is the kind of thing our platform generates on every live call.
// Each call produces a stream of events as it progresses: it starts, it might get put on hold a few times, and eventually it ends. 
// Your job is to figure out how long each call spent on hold in total.
// You'll receive an array of CallEvent objects. The array will always be sorted by timestamp, ascending. Each call starts with a start event and ends with an end event. 
// In between, there can be any number of hold and resume pairs — a hold always precedes its corresponding resume.
// One edge case to be aware of: the caller can hang up while on hold, so you may see a hold followed directly by an end with no resume in between. 
// 
// Treat the time between the hold and end as part of the hold duration.
// The array can contain events from multiple calls, all interleaved, but again, everything is in ascending timestamp order.
// Write a TypeScript function that returns the total hold duration per call, as a record mapping each callId to its total hold time in milliseconds.

interface CallEvent {
    callId: string;
    type: 'start' | 'hold' | 'resume' | 'end';
    timestamp: number; // milliseconds
}

function calculateHoldTime(events: CallEvent[]): Map<string, number> {
    const logs = new Map<string, number>();
    const lastHeld = new Map<string, number>();

    for (const event of events) {
        if (event.type === "hold") {
            lastHeld.set(event.callId, event.timestamp)
        } else if (event.type === "resume" || event.type === "end") {
            const holdStart = lastHeld.get(event.callId)
            if (holdStart === undefined) continue
            logs.set(event.callId, (event.timestamp - holdStart) + (logs.get(event.callId) ?? 0))
            lastHeld.delete(event.callId)
        }
    }

    return logs
}

// Sample — feel free to test against this:
const sample: CallEvent[] = [
    { callId: 'call-1', type: 'start', timestamp: 1744675200000 },
    { callId: 'call-2', type: 'start', timestamp: 1744675202500 },
    { callId: 'call-1', type: 'hold', timestamp: 1744675215000 },
    { callId: 'call-2', type: 'hold', timestamp: 1744675220000 },
    { callId: 'call-1', type: 'resume', timestamp: 1744675232000 },
    { callId: 'call-2', type: 'resume', timestamp: 1744675238000 },
    { callId: 'call-2', type: 'hold', timestamp: 1744675248000 },
    { callId: 'call-1', type: 'hold', timestamp: 1744675255000 },
    { callId: 'call-2', type: 'resume', timestamp: 1744675261000 },
    { callId: 'call-2', type: 'end', timestamp: 1744675270000 },
    { callId: 'call-1', type: 'end', timestamp: 1744675275000 },
];