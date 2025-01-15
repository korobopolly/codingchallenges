using System;

class Program
{
    static void Main(string[] args)
    {
        var input = Console.ReadLine();
        int score = int.Parse(input);
        if (score >= 90 && score <= 100)
        {
            Console.WriteLine("A");
        }
        else if (score >= 80 && score <= 89)
        {
            Console.WriteLine("B");
        }
        else if (score >= 70 && score <= 79)
        {
            Console.WriteLine("C");
        }
        else if (score >= 60 && score <= 69)
        {
            Console.WriteLine("D");
        }
        else {
            Console.WriteLine("F");
        }
    }
}
