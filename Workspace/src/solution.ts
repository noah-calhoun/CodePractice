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

function solution(): void {

}
solution(sample);
