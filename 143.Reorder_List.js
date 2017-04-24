/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function(head) {
	if (!head) return;
	let arr = [];
	let p1 = 0;
	let p2 = -1;
	let signal = true;
	let node = head;
	while (node) {
		p2++;
		arr.push(node);
		node = node.next;
	}
	while (p1 < p2) {
		if (signal) {
			arr[p1].next = arr[p2];
			p1++;
			signal = false;
		} else {
			arr[p2].next = arr[p1];
			p2--;
			signal = true;
		}
	}
	arr[p1].next = null;
};
