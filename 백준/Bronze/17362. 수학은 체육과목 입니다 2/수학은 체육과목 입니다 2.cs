using System;
using System.Collections.Generic; //HashSet을 사용하기 위해 필요
using System.Linq; //Linq를 사용하기 위해 필요
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{
    static void Main(string[] args)
    {
        StringBuilder sb = new StringBuilder();
        int N = int.Parse(Console.ReadLine()) % 8;
        switch (N)
        {
            case 1:
                sb.Append('1'); break;
            case 0:
            case 2:
                sb.Append('2'); break;
            case 3:
            case 7:
                sb.Append('3'); break;
            case 4:
            case 6:
                sb.Append('4'); break;
            case 5:
                sb.Append('5'); break;
            default:
                // 위의 case 조건에 맞지 않을 때 실행할 코드
                break;
        } 
        Console.WriteLine(sb.ToString());
    }
}
