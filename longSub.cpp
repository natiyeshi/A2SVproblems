class Solution {
public:
    
int check(vector<char>col,char x){
    for(int i = 0; i < col.size();i++){
        if(col[i] == x){
            return true;
        }
    }
    return false;
}

    int lengthOfLongestSubstring(string file) {
          int sum = 0;
    for(int i = 0; i < file.length();i++){
        vector<char>col;
        int ln = 0;
        for(int j = i; j < file.length();j++){
            if(check(col,file[j]) == false){
                col.push_back(file[j]);
                ln++;
            } else{
                break;
            }
        }
        
       if(sum < ln){
            sum = ln;
        }
    }    

    return sum;   
    }
};
