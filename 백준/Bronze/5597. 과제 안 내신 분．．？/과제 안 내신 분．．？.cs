using System;
using System.Linq;
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{
    static void Main(string[] args)
    {
        StringBuilder sb = new StringBuilder();
        List<int> list = new List<int>(Enumerable.Range(1, 30).ToArray());
        for (int i = 0; i < 28; i++) {
            list.Remove(int.Parse(Console.ReadLine()));
        }
        list.Sort();
        sb.Append(string.Join(' ', list));
        Console.WriteLine(sb.ToString());
    }
}
