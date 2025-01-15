using System;

class Program
{
    static void Main(string[] args)
    {
        string x = Console.ReadLine();
        string y = Console.ReadLine();
        if (x[0] == '-' && y[0] == '-') {
            Console.WriteLine("3");
        }
        else if (x[0] == '-' && y[0] != '-')
        {
            Console.WriteLine("2");
        }
        else if (x[0] != '-' && y[0] == '-')
        {
            Console.WriteLine("4");
        }
        else
        {
            Console.WriteLine("1");
        }
    }
}
