clc
A = imread('fotogris.jpg');
imshow(A)
A = double(A);
[U,S,V] = svd(A);

for k=1:1:30
    X1=U(:,1:k)*S(1:k,1:k)*(V(:,1:k))';
    imshow(uint8(X1))
end

for k=1:1:150
    X2=U(:,1:k)*S(1:k,1:k)*(V(:,1:k))';
    imshow(uint8(X2))
end






    

