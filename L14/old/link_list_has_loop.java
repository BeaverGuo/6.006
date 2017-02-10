//You can make use of Floyd's cycle-finding algorithm, also know as tortoise and hare algorithm.

//The idea is to have two references to the list and move them at different speeds. Move one forward by 1 node and the other by 2 nodes.

//If the linked list has a loop they will definitely meet.
//Else either of the two references(or their next) will become null.
//Java function implementing the algorithm:

boolean hasLoop(Node first) {

    if(first == null) // list does not exist..so no loop either.
        return false;

    Node slow, fast; // create two references.

    slow = fast = first; // make both refer to the start of the list.

    while(true) {

        slow = slow.next;          // 1 hop.

        if(fast.next != null)
            fast = fast.next.next; // 2 hops.
        else
            return false;          // next node null => no loop.

        if(slow == null || fast == null) // if either hits null..no loop.
            return false;

        if(slow == fast) // if the two ever meet...we must have a loop.
            return true;
    }
}

boolean hasLoop(Node first) {
    Node slow = first;
    Node fast = first;

    while(fast != null && fast.next != null) {
        slow = slow.next;          // 1 hop
        fast = fast.next.next;     // 2 hops 

        if(slow == fast)  // fast caught up to slow, so there is a loop
            return true;
    }
    return false;  // fast reached null, so the list terminates
}


//An alternative solution to the Turtle and Rabbit, 
//not quite as nice, as I temporarily change the list:

//The idea is to walk the list, and reverse it as you go. 
//Then, when you first reach a node that has already been visited, its next pointer will point "backwards", causing the iteration to proceed towards first again, where it terminates.

Node prev = null;
Node cur = first;
while (cur != null) {
    Node next = cur.next;
    cur.next = prev;
    prev = cur;
    cur = next;
}
boolean hasCycle = prev == first && first != null && first.next != null;

// reconstruct the list
cur = prev;
prev = null;
while (cur != null) {
    Node next = cur.next;
    cur.next = prev;
    prev = cur;
    cur = next;
}

return hasCycle;