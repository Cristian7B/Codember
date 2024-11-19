import trace from "./trace";

const allTraces = trace.split("\n");

function calculateTraces(allTraces) {
    let total = 0;
    let lastCount = 0;
    const traces = allTraces.split("\n")

    for (let trace of traces) {
        const numbers = trace.split(" ").map(Number)
        const count = numbers.length
        let actualIndex = 0
        let counter = 0

        while (actualIndex >= 0 && actualIndex < count) {
            const numberActual = numbers[actualIndex]
            numbers[actualIndex] = numberActual + 1 
            actualIndex = numberActual + actualIndex;
            counter += 1;
            if (actualIndex < 0 || actualIndex >= count) break
        }

        total += counter
        lastCount = counter
    }

    console.log(total, lastCount)
}
calculateTraces(allTraces)