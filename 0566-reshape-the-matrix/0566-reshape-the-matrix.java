class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        int m = mat.length;
        int n = mat[0].length;
        
        //exception
        if (m*n != r*c) return mat;
        
        int[][] result = new int[r][c];
        
        int out_r = 0;
        int out_c = 0;
        
        for (int i=0; i < m; i++) {
            
            for (int j=0; j < n; j++) {
                
                result[out_r][out_c] = mat[i][j];
                out_c++;
                
                if (out_c == c) {
                    out_r++;
                    out_c = 0;
                }
            }
        }
        
        return result;
        
    }
}