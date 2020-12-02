package daycode.day1;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map.Entry;

public class TwoSumPlus {
	
	public static void threeSum(ArrayList<Integer> expenseReport) {
		HashMap<Integer, Integer> normalNums = new HashMap<>();
		HashMap<Integer, int[]> sumNums = new HashMap<>();
		for (int num : expenseReport) {
			normalNums.put(num, 0);
			for (Entry<Integer, Integer> entry : normalNums.entrySet()) {

				if (num != entry.getKey()) {
					sumNums.put(num + entry.getKey(), new int[]{num, entry.getKey()} );
				}
			}
			
			if (sumNums.containsKey(2020 - num)) {
				int[] myNums = sumNums.get(2020-num);
				System.out.printf("Nums: %d %d %d \n", num, myNums[0], myNums[1]);
				System.out.printf("Product: %d", num * myNums[0] *myNums[1]);
			}
		}
	}
	
	public static void twoSum(ArrayList<Integer> expenseReport) {
		HashMap<Integer, Integer> normalNums = new HashMap<>();
		for (int num : expenseReport) {
			
			if (normalNums.containsKey(2020 - num)) {
				System.out.printf("Nums: %d %d \n", num, 2020-num);
				System.out.printf("Product: %d", num * (2020-num));
				return;
			}
			normalNums.put(num, 0);
		}
	}

	
	public static void main(String[] args) throws IOException {
		BufferedReader a = new BufferedReader(new FileReader("resources/day1.txt"));
		String nextLine;
		ArrayList<Integer> expenseReport = new ArrayList<>();
		while (true) {
			 nextLine = a.readLine();
			 if (nextLine == null) {
				 break;
			 }
			 //System.out.println(nextLine);
			 int myVal = Integer.parseInt(nextLine);
			 expenseReport.add(myVal);
		} 
		
		System.out.println("Two Sum Answer:");
		twoSum(expenseReport);
		System.out.println("Three Sum Answer:");
		threeSum(expenseReport);
		
		
		
		
	}
}
