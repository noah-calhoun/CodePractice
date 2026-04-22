"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.twoSum = void 0;
function twoSum(nums, target) {
    let map = {};
    for (let i = 0; i < nums.length; i++) {
        let complement = target - nums[i];
        if (map[complement] !== undefined) {
            return [map[complement], i];
        }
        map[nums[i]] = i;
    }
    return [];
}
exports.twoSum = twoSum;
//# sourceMappingURL=twosum.js.map