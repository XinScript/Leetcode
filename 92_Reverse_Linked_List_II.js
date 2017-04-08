/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} m
 * @param {number} n
 * @return {ListNode}
 */
var reverseBetween = function(head, m, n) {

	if(!head) return head;
	let node = head;
	let count = n - m ;
	let p = m-1;
	let n_next = null;
	let m_before = null;
	let new_head = null;
	while (p) {
		m_before = node;
		node = node.next;
		p--;
	}

	function reverse(node) {
		if (count === 0) {
			n_next = node.next;
			new_head = node;
		} else {
			count--;
			reverse(node.next).next = node;
		}
		return node;
	}
	reverse(node).next = n_next;
	if(m_before){
		m_before.next = new_head;
		return head;
	}
	else return new_head;
};