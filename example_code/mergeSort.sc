

val L = List(19,3,14,5,99,8,64,32,11)


def merge(A: List[Int], B: List[Int]): List[Int] =
{
  if (A.isEmpty) B
  else if (B.isEmpty) A
  else if (A.head<B.head) A.head :: merge(A.tail, B)
  else B.head :: merge(A, B.tail)
}


def mergeSort(L: List[Int]): List[Int] =
{
  if (L.length == 1) L
  else
  {
    val (left,right) = L.splitAt(L.length/2)
    merge(mergeSort(left), mergeSort(right))
  }
}


mergeSort(L)

