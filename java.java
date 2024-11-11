//코딩테스트 문제 LV0

//주어진 코드는 변수에 데이터를 저장하고 출력하는 코드입니다. 아래와 같이 출력되도록 빈칸을 채워 코드를 완성해 주세요.

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        String message = "Let's go!";

        System.out.println("3\n2\n1");
        System.out.println(message);
    }
}

//일반적으로 두 선분이 이루는 각도는 한 바퀴를 360도로 하여 표현합니다. 따라서 각도에 360의 배수를 더하거나 빼더라도 같은 각을 의미합니다. 예를 들면, 30도와 390도는 같은 각도입니다.
//주어진 코드는 각도를 나타내는 두 정수 angle1과 angle2가 주어질 때, 이 두 각의 합을 0도 이상 360도 미만으로 출력하는 코드입니다. 코드가 올바르게 작동하도록 한 줄을 수정해 주세요.

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int angle1 = sc.nextInt();
        int angle2 = sc.nextInt();

        int sum_angle = angle1 + angle2;
        System.out.println(sum_angle%360);
    }
}

//2자리 이상의 정수 number가 주어집니다. 주어진 코드는 이 수를 2자리씩 자른 뒤, 자른 수를 모두 더해서 그 합을 출력하는 코드입니다. 코드가 올바르게 작동하도록 한 줄을 수정해 주세요.

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int number = sc.nextInt();
        int answer = 0;
        
        for(int i=0; number!=0; i++){
            answer += number % 100;
            number /= 100;
        }

        System.out.println(answer);
    }
}

// 퓨쳐종합병원에서는 접수한 환자가 진료받을 병과에 따라 자동으로 환자 코드를 부여해 주는 프로그램이 있습니다. 환자 코드의 마지막 네 글자를 보면 환자가 어디 병과에서 진료를 받아야 할지 알 수 있습니다. 예를 들어 환자의 코드가 "_eye"로 끝난다면 안과를, "head"로 끝난다면 신경외과 진료를 보게 됩니다. 환자 코드의 마지막 글자에 따른 병과 분류 기준은 다음과 같습니다.
// 마지막 글자	병과
// "_eye"	"Ophthalmologyc"
// "head"	"Neurosurgery"
// "infl"	"Orthopedics"
// "skin"	"Dermatology"
// 환자의 코드를 나타내는 문자열 code를 입력받아 위 표에 맞는 병과를 출력하도록 빈칸을 채워 코드를 완성해 주세요. 위 표의 단어로 끝나지 않는다면 "direct recommendation"를 출력합니다.

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String code = sc.next();
        String lastFourWords = code.substring(code.length()-4, code.length());

        if(lastFourWords.equals("_eye")){
            System.out.println("Ophthalmologyc");
        }
        else if(lastFourWords.equals("head")){
            System.out.println("Neurosurgery");
        }
        else if(lastFourWords.equals("infl")){
            System.out.println("Orthopedics");
        }
        else if(lastFourWords.equals("skin"))
        {
            System.out.println("Dermatology");
        }
        else
        {
            System.out.println("direct recommendation");
        }
    }
}

// 심폐소생술은 다음과 같은 순서를 통해 실시합니다.
// 심정지 및 무호흡 확인 [check]
// 도움 및 119 신고 요청 [call]
// 가슴압박 30회 시행 [pressure]
// 인공호흡 2회 시행 [respiration]
// 가슴압박, 인공호흡 반복 [repeat]
// 주어진 solution 함수는 심폐소생술을 하는 방법의 순서가 담긴 문자열들이 무작위 순서로 담긴 리스트 cpr이 주어질 때 각각의 방법이 몇 번째 단계인지 순서대로 담아 return하는 함수입니다. solution 함수가 올바르게 작동하도록 빈칸을 채워 solution 함수를 완성해 주세요.

// 제한사항
// cpr은 다음 문자열들이 한 번씩 포함되어 있습니다.
// "check", "call", "pressure", "respiration", "repeat"

class Solution {
    public int[] solution(String[] cpr) {
        int[] answer = {0, 0, 0, 0, 0};
        String[] basic_order = {"check", "call", "pressure", "respiration", "repeat"};

        for(int i=0; i<cpr.length; i++){
            for(int j=0; j<basic_order.length; j++){
                if(cpr[i].equals(basic_order[j])){
                    answer[i] = j+1;
                    break;
                }
            }
        }
        return answer;
    }
}

// ㅇㅇ시에서는 저수지가 하나 있는데, 도시 내에서 사용하는 모든 물은 이 저수지에 저장된 물을 끌어와 사용합니다. 이상 기후로 인해 극심한 가뭄이 예고된 상황에서, 지난 달의 물 사용량과 이번달부터 일정 기간 동안의 월별 물 사용량의 변화를 예측한 값을 이용해 몇 달 뒤 물이 부족해지는지 예측하려고 합니다.
// 이번달부터의 월별 물 사용량 변화를 예측한 값은 다음과 같이 리스트에 담겨 주어집니다.
// [10, -10, 10, -10, 10, -10, 10, -10, 10, -10]
// 리스트의 각 원소는 해당 월의 물 사용량이 전 달에 비해 몇 % 만큼 증가 또는 감소하는지를 나타냅니다.
// 예를 들어, 이번달의 물 사용량 (리스트의 첫 번째 원소)은 지난 달 보다 10% 증가한 값이며, 다음 달(리스트의 두 번째 원소)의 물 사용량은 이번달 사용량에서 10%만큼 감소한 값입니다.
// 자세한 값은 입출력 예시를 참고해 주세요.
// 현재 저수지에 저장된 물의 양을 나타내는 정수 storage와 지난 달 물 사용량을 나타내는 정수 usage, 월별 물 사용량이 전 달 대비 어떻게 변하는지 저장된 정수 리스트 change가 주어질 때 몇 달 뒤 물이 부족해지는지 return 하도록 solution 함수를 작성하려 합니다. 코드가 올바르게 작동하도록 한 줄을 수정해 solution 함수를 완성해 주세요. 가뭄이 끝날때 까지 저수지의 물이 남아 있다면 -1을 return합니다.

// 제한사항
// 1,000 ≤ storage ≤ 1,000,000
// 500 ≤ usage ≤ 30,000
// 1 ≤ change의 길이 ≤ 30
// -99 ≤ change[i] ≤ 500
// change[i] 가 양수일 경우 물 사용량은 전 달 보다 change[i]% 만큼 증가합니다.
// change[i] 가 음수일 경우 물 사용량은 전 달 보다 change[i]% 만큼 감소합니다.
// change[i] 가 0일 경우 물 사용량은 전 달과 동일합니다.
// 매달 물 사용량은 소수점 이하를 버린 정수로 계산합니다.
// 입출력 예
// storage	usage	change	result
// 5141	500	[10, -10, 10, -10, 10, -10, 10, -10, 10, -10]	-1
// 1000	2000	[-10, 25, -33]	1

class Solution {
    public int solution(int storage, int usage, int[] change) {
        int total_usage = 0;
        for(int i=0; i<change.length; i++){
            usage += usage * change[i] / 100;
            total_usage += usage;
            if(total_usage > storage){
                return i;
            }
        }
        return -1;
    }
}

// 영진이는 약속장소에 가기 위해 버스를 타려고 합니다. 버스에는 좌석이 총 seat개만큼 있습니다. 영진이는 버스 좌석에 앉아서 갈 수 있을지 궁금해합니다. 기점에서 출발한 버스가 영진이가 기다리는 정거장에 도착하기 전에 방문하는 각 정거장에서 승/하차한 승객 정보가 주어질 때, 영진이가 버스에 탄 순간 빈 좌석은 몇 개인지 구해주세요. 영진이가 기다리는 정거장에서는 영진이가 제일 먼저 버스에 탑승하며, 이전 정거장에서 버스에 탑승한 승객들은 남는 좌석이 있다면 항상 앉는다고 가정합니다. 또, 기점에서 출발하는 버스에는 승객이 0명 타고 있습니다.
// 예를 들어 다음은 좌석이 5개인 버스에 각 정거장에서 승/하차한 승객 정보를 나타냅니다. 영진이는 4번 정거장에서 기다리고 있으며, "On"은 승차한 승객, "Off"는 하차한 승객을 의미합니다.
// - 1번 정거장 : ["On", "On", "On"] (3명 승차, 0명 하차)
// - 2번 정거장 : ["Off", "On", "-"] (1명 승차, 1명 하차)
// - 3번 정거장 : ["Off", "-", "-"]  (0명 승차, 1명 하차)
// 위와 같은 경우, 1번 정거장에서 3명이 승차하고, 2번 정거장에서 1명 승차 1명 하차, 3번 정거장에서 1명이 하차했으므로 4번 정거장에 도착한 버스에는 2명이 타고 있습니다. 4번 정거장에서는 영진이가 가장 먼저 탑승하므로, 남아있는 좌석 수는 3개입니다.
// 주어진 solution함수는 버스의 좌석 개수 seat, 기점에서 출발한 버스가 순서대로 방문한 정거장에서 승객이 승/하차한 정보를 담은 2차원 문자열 리스트 passengers가 주어질 때, 버스에 남아있는 좌석의 개수를 return 하는 함수입니다. solution 함수가 올바르게 작동하도록 빈칸을 채워 solution함수를 완성해 주세요.

class Solution {
    public int solution(int seat, String[][] passengers) {
        int num_passenger = 0;
        for(int i=0; i<passengers.length; i++){
            num_passenger += func4(passengers[i]);
            num_passenger -= func3(passengers[i]);
        }
        int answer = func1(seat - num_passenger);
        return answer;
    }

    public int func1(int num){
        if(0 > num){
            return 0;
        }
        else{
            return num;
        }
    }
    public int func2(int num){
        if(num > 0){
            return 0;
        }
        else{
            return num;
        }
    }

    public int func3(String[] station){
        int num = 0;
        for(int i=0; i<station.length; i++){
            if(station[i].equals("Off")){
                num += 1;
            }
        }
        return num;
    }

    public int func4(String[] station){
        int num = 0;
        for(int i=0; i<station.length; i++){
            if(station[i].equals("On")){
                num += 1;
            }
        }
        return num;
    }
}

// 온라인 서비스를 이용하기 위해서 닉네임이 필요합니다. 이때 닉네임이 될 수 있는 조건은 다음과 같습니다.
// 닉네임의 길이가 4자 이상 8자 이하여야합니다.
// 닉네임에는 소문자 l과w, 대문자 O와 W를 사용할 수 없습니다.
// 이외의 영어 대소문자와 숫자는 모두 사용이 가능합니다.
// 주어진 solution 함수는 사용할 수 없는 닉네임 nickname을 받아 사용할 수 있는 닉네임으로 바꿔주는 함수입니다. 이때 닉네임을 변경하는 규칙은 다음과 같으며 첫 번째 규칙부터 순서대로 적용합니다.
// 소문자 l을 대문자 I로 변경합니다.
// 소문자 w를 두 개의 소문자 v, 즉 vv로 변경합니다.
// 대문자 W를 두 개의 대문자 V, 즉 VV로 변경합니다.
// 대문자 O를 숫자 0으로 변경합니다.
// 수정된 닉네임의 길이가 4 미만일 경우 뒤에 소문자 o를 길이가 4가 될때까지 이어붙입니다.
// 수정된 닉네임의 길이가 8보다 클 경우 8번째 문자까지만 사용합니다.
// 주어진 solution 함수에는 위의 규칙 중 올바르게 적용되지 않는 것이 있습니다. solution 함수가 올바르게 작동하도록 한 줄을 수정해주세요.

class Solution {
    public String solution(String nickname) {
        String answer = "";
        for(int i=0; i<nickname.length(); i++){
            if(nickname.charAt(i) == 'l'){
                answer += "I";
            }
            else if(nickname.charAt(i) == 'w'){
                answer += "vv";
            }
            else if(nickname.charAt(i) == 'W'){
                answer += "VV";
            }
            else if(nickname.charAt(i) == 'O'){
                answer += "0";
            }
            else{
                answer += nickname.charAt(i);
            }
        }
        while(answer.length() < 4){
            answer += "o";
        }
        if(answer.length() > 8){
            answer = answer.substring(0, 8);
        }
        return answer;
    }
}

// 주어진 초기 코드는 변수에 데이터를 저장하고 출력하는 코드입니다. 아래와 같이 출력되도록 빈칸을 채워 코드를 완성해 주세요.
// 출력 예시
// Spring is beginning
// 13
// 310

#include <iostream>

using namespace std;

int main(void) {
    string msg = "Spring is beginning";
    int val1 = 3;
    string val2 = "3";

    cout << msg << endl;
    cout << val1 + 10 << endl;
    cout << val2 + "10" << endl;

    return 0;
}

// 직각삼각형이 주어졌을 때 빗변의 제곱은 다른 두 변을 각각 제곱한 것의 합과 같습니다.
// 피타고라스.jpg
// 직각삼각형의 한 변의 길이를 나타내는 정수 a와 빗변의 길이를 나타내는 정수 c가 주어질 때, 다른 한 변의 길이의 제곱, b_square 을 출력하도록 한 줄을 수정해 코드를 완성해 주세요.

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int c = sc.nextInt();

        int b_square = (int)Math.pow(c,2) - (int)Math.pow(a,2);

        System.out.println(b_square);
    }
}

// 나이를 세는 방법은 여러 가지가 있습니다. 그중 한국식 나이는 태어난 순간 1살이 되며 해가 바뀔 때마다 1살씩 더 먹게 됩니다. 연 나이는 태어난 순간 0살이며 해가 바뀔 때마다 1살씩 더 먹게 됩니다. 각각 나이의 계산법은 다음과 같습니다.
// 한국식 나이 : 현재 연도 - 출생 연도 + 1
// 연 나이 : 현재 연도 - 출생 연도
// 출생 연도를 나타내는 정수 year와 구하려는 나이의 종류를 나타내는 문자열 age_type이 주어질 때 2030년에 몇 살인지 출력하도록 빈칸을 채워 코드를 완성해 주세요. age_type이 "Korea"라면 한국식 나이를, "Year"라면 연 나이를 출력합니다.

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int year = sc.nextInt();
        String age_type = sc.next();
        int answer = 0;

        if (age_type.equals("Korea")) {
            answer = 2030 - year + 1;
        }
        else if (age_type.equals("Year")) {
            answer = 2030 - year;
        }

        System.out.println(answer);
    }
}

// 진우는 돈을 모으기 위해 저축을 하려고 합니다. 목표로 하는 금액은 100만 원이며, 첫 달에 일정 금액을 넣은 뒤 70만 원까지는 매월 조금씩 저축하다가 70만 원 이후부터는 월 저축량을 늘려 빠르게 목표 금액을 달성하고자 합니다.
// 첫 달에 저축하는 금액을 나타내는 정수 start, 두 번째 달 부터 70만 원 이상 모일 때까지 매월 저축하는 금액을 나타내는 정수 before, 100만 원 이상 모일 때 까지 매월 저축하는 금액을 나타내는 정수 after가 주어질 때, 100만 원 이상을 모을 때까지 걸리는 개월 수를 출력하도록 빈칸을 채워 코드를 완성해 주세요.

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int start = sc.nextInt();
        int before = sc.nextInt();
        int after = sc.nextInt();

        int money = start;
        int month = 1;
        while (money < 70) {
            money += before;
            month++;
        }
        while (money  < 100) {
            money += after;
            month++;
        }

        System.out.println(month);
    }
}

// 여름이는 강아지를 산책시키려고 합니다. 여름이는 2차원 좌표평면에서 동/서/남/북 방향으로 1m 단위로 이동하면서 강아지를 산책시킵니다. 산책루트가 담긴 문자열 route가 주어질 때, 도착점의 위치를 return하도록 빈칸을 채워 solution함수를 완성해 주세요.
// route는 "N", "S", "E", "W"로 이루어져 있습니다.
// "N"은 북쪽으로 1만큼 움직입니다.
// "S"는 남쪽으로 1만큼 움직입니다.
// 북쪽으로 -1만큼 움직인 것과 같습니다.
// "E"는 동쪽으로 1만큼 움직입니다.
// "W"는 서쪽으로 1만큼 움직입니다.
// 동쪽으로 -1만큼 움직인 것과 같습니다.
// 출발점으로부터 [동쪽으로 떨어진 거리, 북쪽으로 떨어진 거리]형태로 강아지의 최종 위치를 구해서 return해야 합니다.
// 출발점을 기준으로 서쪽, 남쪽에 있는 경우는 동쪽, 북쪽으로 음수만큼 떨어진 것으로 표현합니다.
// 출발점으로부터 동쪽으로 2, 북쪽으로 3만큼 떨어졌다면 [2, 3]을 return 합니다.
// 출발점으로부터 서쪽으로 1, 남쪽으로 4만큼 떨어졌다면 [-1, -4]를 return 합니다.

class Solution {
    public int[] solution(String route) {
        int east = 0;
        int north = 0;
        int[] answer = new int [2];
        for(int i=0; i<route.length(); i++){
            switch(route.charAt(i)){
                case 'N':
                    north++;
                    break;
                case 'S':
                    north--;
                    break;
                case 'E':
                    east++;
                    break;
                case 'W':
                    east--;
                    break;
            }
        }
        answer[0] = east;
        answer[1] = north;
        return answer;
    }
}

// A반 학생들은 시험이 끝난 뒤 성적이 나오기 전 자기 시험지를 가채점해 보았습니다. 이후에 선생님이 실제 성적을 불러 줄 때 가채점한 점수와 실제 성적이 다른 학생들이 있어 선생님께 문의를 하려고 합니다.
// 성적을 문의하려는 학생들의 번호가 담긴 정수 리스트 numbers와 가채점한 점수가 성적을 문의하려는 학생 순서대로 담긴 정수 리스트 our_score, 실제 성적이 번호 순서대로 담긴 정수 리스트 score_list가 주어집니다. 주어진 solution 함수는 가채점한 점수가 실제 성적과 동일하다면 "Same"을, 다르다면 "Different"를 순서대로 리스트에 담아 return하는 함수입니다. solution 함수가 올바르게 작동하도록 한 줄을 수정해 주세요.

class Solution {
    public String[] solution(int[] numbers, int[] our_score, int[] score_list) {
        int num_student = numbers.length;
        String[] answer = new String[num_student];

        for (int i = 0; i < num_student; i++) {
            if (our_score[i] == score_list[numbers[i]-1]) {
                answer[i] = "Same";
            }
            else {
                answer[i] = "Different";
            }
        }

        return answer;
    }
}

// 상우가 사용하는 가습기에는 "auto", "target", "minimum"의 세 가지 모드가 있습니다. 가습기의 가습량은 0~5단계로 구분되며 각 모드 별 동작 방식은 다음과 같습니다.
// "auto" 모드
// 습도가 0 이상 10 미만인 경우 : 5단계
// 습도가 10 이상 20 미만인 경우 : 4단계
// 습도가 20 이상 30 미만인 경우 : 3단계
// 습도가 30 이상 40 미만인 경우 : 2단계
// 습도가 40 이상 50 미만인 경우 : 1단계
// 습도가 50 이상인 경우 : 0단계
// "target" 모드
// 습도가 설정값 미만일 경우 : 3단계
// 습도가 설정값 이상일 경우 : 1단계
// "minimum"모드
// 습도가 설정값 미만일 경우 : 1단계
// 습도가 설정값 이상일 경우 : 0단계
// 상우가 설정한 가습기의 모드를 나타낸 문자열 mode_type, 현재 공기 중 습도를 나타낸 정수 humidity, 설정값을 나타낸 정수 val_set이 주어질 때 현재 가습기가 몇 단계로 작동 중인지 return하도록 빈칸을 채워 solution 함수를 완성해 주세요.

class Solution {
    public int func1(int humidity, int val_set){
        if(humidity < val_set)
            return 3;
        return 1;
    }

    public int func2(int humidity){
        if(humidity >= 50)
            return 0;
        else if (humidity >= 40)
            return 1;
        else if (humidity >= 30)
            return 2;
        else if (humidity >= 20)
            return 3;
        else if (humidity >= 10)
            return 4;       
        else
            return 5;
    }

    public int func3(int humidity, int val_set){
        if(humidity < val_set)
            return 1;
        return 0;
    }

    public int solution(String mode_type, int humidity, int val_set) {
        int answer = 0;

        if(mode_type.equals("auto")){
            answer = func2(humidity);
        }
        else if(mode_type.equals("target")){
            answer = func1(humidity,val_set);
        }
        else if(mode_type.equals("minimum")){
            answer = func3(humidity,val_set);
        }

        return answer;
    }
}

// 선빈이는 게임을 즐기던 중 가지고 있는 물건이 너무 많아 창고 정리를 하기로 했습니다. 선빈이가 보유한 게임 속 창고는 여러 칸으로 나누어져 있고 각 칸에는 물건들이 담겨있습니다. 창고를 정리할 방법을 고민하던 선빈이는 같은 물건이 여러 칸에 나누어 들어있는 것을 발견하고 우선 같은 물건끼리 최대한 겹쳐쌓는 방식으로 창고를 정리하기로 했습니다. 선빈이의 창고에 들어있는 물건의 이름과 개수는 리스트 형태로 주어지며, 한 칸에 겹쳐질 수 있는 물건의 개수에는 제한이 없다고 가정합니다.
// 예를 들어 창고의 각 칸에 담겨있는 물건의 이름이storage = ["pencil", "pencil", "pencil", "book"], 각 물건의 개수가 num = [2, 4, 3, 1]이라면 연필과 책을 한 칸에 각각 겹쳐 쌓아 간단하게 clean_storage = ["pencil", "book"], clean_num = [9, 1]로 만들 수 있습니다.
// pencil book javacpp.jpg
// 주어진 solution 함수는 정리되기 전 창고의 물건 이름이 담긴 문자열 리스트 storage와 각 물건의 개수가 담긴 정수 리스트 num이 주어질 때, 정리된 창고에서 개수가 가장 많은 물건의 이름을 return 하는 함수입니다. solution 함수가 올바르게 작동하도록 한 줄을 수정해 주세요.

class Solution {
    public String solution(String[] storage, int[] num) {
        int num_item = 0;
        String[] clean_storage = new String[storage.length];
        int[] clean_num = new int[num.length];
        
        for(int i=0; i<storage.length; i++){
            int clean_idx = -1;
            for(int j=0; j<num_item; j++){
                if(storage[i].equals(clean_storage[j])){
                    clean_idx = j;
                    break;
                }
            }
            if(clean_idx == -1){
                clean_storage[num_item] = storage[i];
                clean_num[num_item] = num[i];
                num_item += 1;
            }
            else{
                clean_num[clean_idx] += num[i];
            }
        }
        
        // 아래 코드에는 틀린 부분이 없습니다.
        
        int num_max = -1;
        String answer = "";
        for(int i=0; i<num_item; i++){
            if(clean_num[i] > num_max){
                num_max = clean_num[i];
                answer = clean_storage[i];
            }
        }
        return answer;
    }
}

//코딩테스트 문제 LV1
// 당신은 동영상 재생기를 만들고 있습니다. 당신의 동영상 재생기는 10초 전으로 이동, 10초 후로 이동, 오프닝 건너뛰기 3가지 기능을 지원합니다. 각 기능이 수행하는 작업은 다음과 같습니다.
// 10초 전으로 이동: 사용자가 "prev" 명령을 입력할 경우 동영상의 재생 위치를 현재 위치에서 10초 전으로 이동합니다. 현재 위치가 10초 미만인 경우 영상의 처음 위치로 이동합니다. 영상의 처음 위치는 0분 0초입니다.
// 10초 후로 이동: 사용자가 "next" 명령을 입력할 경우 동영상의 재생 위치를 현재 위치에서 10초 후로 이동합니다. 동영상의 남은 시간이 10초 미만일 경우 영상의 마지막 위치로 이동합니다. 영상의 마지막 위치는 동영상의 길이와 같습니다.
// 오프닝 건너뛰기: 현재 재생 위치가 오프닝 구간(op_start ≤ 현재 재생 위치 ≤ op_end)인 경우 자동으로 오프닝이 끝나는 위치로 이동합니다.
// 동영상의 길이를 나타내는 문자열 video_len, 기능이 수행되기 직전의 재생위치를 나타내는 문자열 pos, 오프닝 시작 시각을 나타내는 문자열 op_start, 오프닝이 끝나는 시각을 나타내는 문자열 op_end, 사용자의 입력을 나타내는 1차원 문자열 배열 commands가 매개변수로 주어집니다. 이때 사용자의 입력이 모두 끝난 후 동영상의 위치를 "mm:ss" 형식으로 return 하도록 solution 함수를 완성해 주세요.

class Solution {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        String answer = pos; // 초기 시간으로 설정

        // 1. 최초에 op_start와 op_end 범위 안에 있는지 확인
        if (isWithinRange(answer, op_start, op_end)) {
            answer = op_end;
        }

        // 2. commands 배열을 순회하며 prev, next 명령 처리
        for (int i = 0; i < commands.length; i++) {
            if (commands[i].equals("prev")) {
                answer = adjustTime(answer, -10); // 10초 감소
            } else if (commands[i].equals("next")) {
                answer = adjustTime(answer, 10); // 10초 증가
            }

            // 3. 매 명령 후 op_start와 op_end 범위 안에 있으면 op_end로 설정
            if (isWithinRange(answer, op_start, op_end)) {
                answer = op_end;
            }

            // 4. video_len을 넘지 않도록 제한
            if (isGreaterThan(answer, video_len)) {
                answer = video_len;
            }
        }

        return answer;
    }

    // 주어진 시간(time)이 op_start와 op_end 범위 안에 있는지 확인하는 메서드
    private boolean isWithinRange(String time, String op_start, String op_end) {
        return time.compareTo(op_start) >= 0 && time.compareTo(op_end) <= 0;
    }

    // 시간(time)이 video_len을 초과하는지 확인하는 메서드
    private boolean isGreaterThan(String time, String limit) {
        return convertToSeconds(time) > convertToSeconds(limit);
    }

    // 시간을 MM:SS 형식에서 초로 변환하는 메서드
    private int convertToSeconds(String time) {
        String[] timeParts = time.split(":");
        int minutes = Integer.parseInt(timeParts[0]);
        int seconds = Integer.parseInt(timeParts[1]);
        return minutes * 60 + seconds;
    }

    // 특정 시간에서 초를 더하거나 빼는 메서드
    private String adjustTime(String time, int secondsToAdjust) {
        // 1. 시간 문자열을 분과 초로 분리
        String[] timeParts = time.split(":");
        int minutes = Integer.parseInt(timeParts[0]);
        int seconds = Integer.parseInt(timeParts[1]);

        // 2. 전체 초로 변환 후 초를 더하거나 빼기
        int totalSeconds = (minutes * 60) + seconds + secondsToAdjust;

        // 3. 결과가 0보다 작은 경우 0초로 설정
        if (totalSeconds < 0) {
            totalSeconds = 0;
        }

        // 4. 분과 초로 다시 변환
        int newMinutes = totalSeconds / 60;
        int newSeconds = totalSeconds % 60;

        // 5. "MM:SS" 형식으로 반환
        return String.format("%02d:%02d", newMinutes, newSeconds);
    }
}

// 민수는 다양한 지폐를 수집하는 취미를 가지고 있습니다. 지폐마다 크기가 달라 지갑에 넣으려면 여러 번 접어서 넣어야 합니다. 예를 들어 지갑의 크기가 30 * 15이고 지폐의 크기가 26 * 17이라면 한번 반으로 접어 13 * 17 크기로 만든 뒤 90도 돌려서 지갑에 넣을 수 있습니다. 지폐를 접을 때는 다음과 같은 규칙을 지킵니다.
// 지폐를 접을 때는 항상 길이가 긴 쪽을 반으로 접습니다.
// 접기 전 길이가 홀수였다면 접은 후 소수점 이하는 버립니다.
// 접힌 지폐를 그대로 또는 90도 돌려서 지갑에 넣을 수 있다면 그만 접습니다.
// 지갑의 가로, 세로 크기를 담은 정수 리스트 wallet과 지폐의 가로, 세로 크기를 담은 정수 리스트 bill가 주어질 때, 지갑에 넣기 위해서 지폐를 최소 몇 번 접어야 하는지 return하도록 solution함수를 완성해 주세요.
// 지폐를 지갑에 넣기 위해 접어야 하는 최소 횟수를 구하는 과정은 다음과 같습니다.
// 1. 지폐를 접은 횟수를 저장할 정수 변수 answer를 만들고 0을 저장합니다.
// 2. 반복문을 이용해 bill의 작은 값이 wallet의 작은 값 보다 크거나 bill의 큰 값이 wallet의 큰 값 보다 큰 동안 아래 과정을 반복합니다.
//     2-1. bill[0]이 bill[1]보다 크다면
//         bill[0]을 2로 나누고 나머지는 버립니다.
//     2-2. 그렇지 않다면
//         bill[1]을 2로 나누고 나머지는 버립니다.
//     2-3. answer을 1 증가시킵니다.
// 3. answer을 return합니다.
// 위의 의사코드와 작동방식이 다른 코드를 작성해도 상관없습니다.

class Solution {
    public int solution(int[] wallet, int[] bill) {
        int answer = 0;
        
        while(bill[compare(bill, 0)] > wallet[compare(wallet, 0)] || bill[compare(bill, 1)] > wallet[compare(wallet, 1)]){
            if(bill[0]>bill[1])
                bill[0] = bill[0]/2;
            else
                bill[1] = bill[1]/2;
            answer++;
        }
        
        return answer;
    }
    
    // 배열에서 최대값 또는 최소값의 인덱스를 반환하는 메서드
    private int compare(int[] array, int max) { 
        int arraynum = 0;
        
        // max가 1이면 최대값의 인덱스, 0이면 최소값의 인덱스를 반환
        if (max == 1) {
            arraynum = array[1] > array[0] ? 1 : 0;
        } else {
            arraynum = array[1] < array[0] ? 1 : 0;
        }
        
        return arraynum;
    }
}

// 지민이는 다양한 크기의 정사각형 모양 돗자리를 가지고 공원에 소풍을 나왔습니다. 공원에는 이미 돗자리를 깔고 여가를 즐기는 사람들이 많아 지민이가 깔 수 있는 가장 큰 돗자리가 어떤 건지 확인하려 합니다. 예를 들어 지민이가 가지고 있는 돗자리의 한 변 길이가 5, 3, 2 세 종류이고, 사람들이 다음과 같이 앉아 있다면 지민이가 깔 수 있는 가장 큰 돗자리는 3x3 크기입니다.
// 지민이가 가진 돗자리들의 한 변의 길이들이 담긴 정수 리스트 mats, 현재 공원의 자리 배치도를 의미하는 2차원 문자열 리스트 park가 주어질 때 지민이가 깔 수 있는 가장 큰 돗자리의 한 변 길이를 return 하도록 solution 함수를 완성해 주세요. 아무런 돗자리도 깔 수 없는 경우 -1을 return합니다.

import java.util.Arrays;

class Solution {
    public int solution(int[] mats, String[][] park) {
        // 1. 큰 돗자리부터 사용하기 위해 내림차순으로 정렬
        Arrays.sort(mats);
        int rows = park.length;
        int cols = park[0].length;
        
        // 2. 큰 돗자리부터 하나씩 시도
        for (int i = mats.length - 1; i >= 0; i--) {
            int size = mats[i];
            if (canPlaceMat(size, park, rows, cols)) {
                return size;  // 가장 큰 크기의 돗자리를 놓을 수 있으면 바로 반환
            }
        }

        return -1;  // 아무 돗자리도 놓을 수 없는 경우
    }

    // 특정 크기의 돗자리를 놓을 수 있는지 확인하는 메서드
    private boolean canPlaceMat(int size, String[][] park, int rows, int cols) {
        // park의 모든 시작 위치에 대해 size x size 공간이 모두 "-1"인지 확인
        for (int r = 0; r <= rows - size; r++) {
            for (int c = 0; c <= cols - size; c++) {
                if (isPlaceable(r, c, size, park)) {
                    return true;
                }
            }
        }
        return false;
    }

    // (startRow, startCol) 위치에서 size x size 돗자리를 놓을 수 있는지 확인하는 메서드
    private boolean isPlaceable(int startRow, int startCol, int size, String[][] park) {
        for (int r = startRow; r < startRow + size; r++) {
            for (int c = startCol; c < startCol + size; c++) {
                if (!park[r][c].equals("-1")) {  // "-1"가 아닌 경우 해당 위치에 돗자리를 놓을 수 없음
                    return false;
                }
            }
        }
        return true;
    }
}
