using System;

class Program
{
    static void Main(string[] args)
    {
        var numbers = Console.ReadLine().Split();
        int A = int.Parse(numbers[0]);
        int B = int.Parse(numbers[1]);
        if (A > B)
        {
            Console.WriteLine(">");
        }
        else if (A < B)
        {
            Console.WriteLine("<");
        }
        else
        {
            Console.WriteLine("==");
        }
    }
}
