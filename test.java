/*giai phuong trinh bac nhat*/

public class test{

	public static int giaiPTB1(int a, int b){
		try{
			return -b/a;
		} catch(Exception e){
			return 0;
		}
	}

	public static void test1(){
		int result = giaiPTB1(1,1);
		if(result == -1){
			System.out.println("test1 was success!");
		}
		else{
			System.out.println("test1 was failed!");
		}
	}

	public static void test2(){
		int result = giaiPTB1(10,-90);
		if(result == 9){
			System.out.println("test2 was success!");
		}
		else{
			System.out.println("test2 was failed!");
		}
	}

	public static void test3(){
		int result = giaiPTB1(0,1);
		if(result == 0){
			System.out.println("test3 was success!");
		}
		else{
			System.out.println("test3 was failed!");
		}
	}
	public static void main(String [] args){
		//System.out.print("Giai phuong trinh bac nhat!");

		//chay test 1
		test1();

		//chay test 2
		test2();

		//chay test 3
		test3();
	}
}