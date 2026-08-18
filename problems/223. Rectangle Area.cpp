/*
=== 223. Rectangle Area ===

Find the total area covered by two rectilinear rectangles in a 2D plane.
Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Example:
    Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
    Output: 45
*/
// === 12ms(22.22%) === //
int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
    int s1 = (C-A)*(D-B);
    int s2 = (G-E)*(H-F);
    int s3;
    if(E>=C || G<=A || F>=D || B>=H){
        s3 = 0;
    }
    else if((A<=E && B<=F) && (C>=G && D>=H)){
        s3 = s2;
    }
    else if((A>=E && B>=F) && (C<=G && D<=H)){
        s3 = s1;
    }
    else{
        int a = A > E ? A : E;
        int b = B > F ? B : F;
        int c = C < G ? C : G;
        int d = D < H ? D : H;
        s3 = (c-a)*(d-b);
    }
    return s1+s2-s3;
}
// === 8ms(100%) === //
int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
    int s1 = (C-A)*(D-B);
    int s2 = (G-E)*(H-F);
    int s3;
    int a = A > E ? A : E;
    int b = B > F ? B : F;
    int c = C < G ? C : G;
    int d = D < H ? D : H;
    int h = d > b ? d-b : 0;
    int w = c > a ? c-a : 0;
    s3 = h*w;
    return s1+s2-s3;
}