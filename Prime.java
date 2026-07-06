
import java.util.*;


public class Prime {
    boolean[] bool;
    List<Integer>  prime(int n){
        List<Integer> list = new ArrayList<>();
        bool = new boolean[n];
        for(int i = 2;i*i<n;i++){
            if (bool[i]==false){
                for(int j =i*i;j<n;j=j+i){
                    if(j%i==0){
                        bool[j]=true;
                    }
                }
            }
        }
        for(int i =2; i<bool.length;i++){
            if(bool[i]==false){
                list.add(i);
            }
        }
        return list;
    }
    public static void main(String[] args) {
        Prime obj = new Prime();
        System.out.println(obj.prime(100));
    }
}
