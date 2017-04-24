/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
  let num1='';
  let num2='';
  while(l1){
  	num1+=l1.val.toString();
  	l1=l1.next;
  }
  while(l2){
  	num2+=l2.val.toString();
  	l2=l2.next;
  }
  const s = (parseInt(num1)+parseInt(num2)).toString();
  const head = new ListNode(parseInt(s[0]));
  let current = head;
  for(let i =1;i<s.length;i++){
  	current.next = new ListNode(parseInt(s[i]));
  	current = current.next;
  }
  return head;
};