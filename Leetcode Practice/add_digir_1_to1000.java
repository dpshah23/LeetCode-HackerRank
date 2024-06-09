class example{
    public static void main(String[] args) {
        for(int i=1;i<1001;i++){
            int tempnum=i;
            int sum=0;
            while(tempnum!=0){
                int mod=tempnum%10;
                sum+=mod;
                tempnum/=10;
}
System.out.println(i+" : "+sum);
        }
    }
}