#include <bits/stdc++.h>
using namespace std;

struct node{
int arr[8];
struct node *next;
};
struct node *front = NULL;
struct node *rear = NULL;
struct node* temp;
void push(int val,int ar[]) {
int count =0;
   if (rear == NULL) 
   {
      rear = (struct node *)malloc(sizeof(struct node));
      rear->next = NULL;
      for(int i=0;i<8;i++)
      {
      if(ar[i]==0 && count==0)
      {
        rear->arr[i]=val;
        count++;
      }
      else
      {
        rear->arr[i]=ar[i];
      }
      }
      front = rear;
   } 
   else
    {
      temp=(struct node *)malloc(sizeof(struct node));
      rear->next = temp;
       for(int i=0;i<8;i++)
        {
          if(ar[i]==0 && count==0)
            {
              temp->arr[i]=val;
              count++;
            }
          else
            {
              temp->arr[i]=ar[i];
            }
      }
      temp->next = NULL;
      rear = temp;
   }
}
int *pop() {
   temp = front;
   if (temp->next != NULL)
    {
      front=front->next;
      return temp->arr;
    }
    else
    {
      temp = front;
      front = NULL;
      rear = NULL;
      return temp->arr;
    }
   
}
void show(int b[8][8],int ls[])
{
  for(int i=0;i<8;i++)
  {
  b[i][ls[i]-1]=1;
  }
    for (int i = 0; i < 8; i++)
    {
        for (int j = 0; j < 8; j++)
            cout <<b[i][j]<<" ";
        cout << endl;
    }
    exit(0);

}

bool clean(int b[8][8], int cols, int l[8])
{
int count = 0;

    int i, j,rows,b1[8][8]={(0,0)};

    for(int i=0;i<8;i++)
    {
      if(l[i]==0 && count==0)
      {
        rows=i;
        break;  
      }
      if(l[i]!=0)
      {
        b1[i][l[i]-1]=1;
      }
    }
    for (i = 0; i < rows; i++)
        if (b1[i][cols])
            return false;

    for (i = rows, j = cols; i >= 0 && j >= 0; i--, j--)
        if (b1[i][j])
            return false;

    for (i = rows, j = cols; i >= 0 && j < 8; i--, j++)
        if (b1[i][j])
            return false;
           
    if(rows==7)
    {
      l[rows]=cols+1;
      show(b,l);
    }

    return true;
}

void solve(int b[8][8],bool cond)
{
    int arr[8]= {0};
      if(!cond)
        {
          int *ptr;
          ptr = pop();
          for(int i=0;i<8;i++)
            {
              arr[i]=*ptr;
              ptr++;
            }

          for(int i=0;i<8;i++)
          {
            if(clean(b,i,arr))
              {
                push(i+1,arr);
              }
          }
      }

    if(cond)
    {
      for (int i = 0; i < 8; i++)
      {
          push(i+1,arr);
      }
      cond=false;
    }
    solve(b,cond);
}

int main()
{

    int b[8][8] = {(0,0)};
    solve(b, true);
   
    return 0;
}
