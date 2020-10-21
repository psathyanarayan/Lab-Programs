//Implement a circular queue using arrays with the operations:
//Insert an element to the queue.
//Delete an elements from the queue.
//Display the contents of the queue after each operation.
#include<stdio.h>
#include<stdlib.h>
int isFull()
{

}
int isEmpty()
{
    
}
int enqueue(int x)
{
    if(!isEmpty())
    scanf("%d",&x);
    else
    {
        printf("Underflow");
    }
    
}
int dequeue()
{

}
int main()
{
    int front,rear,MAXSIZE,cq[50],n,i;
    front = rear = -1;
    scanf("%d",&n);
    for (i = 0; i < n; i++)
    {
        enqueue(cq[i]);
    }
    
    return 0;
}

