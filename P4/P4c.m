clc
B = imread('IMG_1582.TIF');
B1 = double(B);
[U,S,V] = svd(B1);

for k=1:1:10
    X1=U(:,1:k)*S(1:k,1:k)*(V(:,1:k))';
    imshow(uint8(X1))
end
for k=1:1:30
    X2=U(:,1:k)*S(1:k,1:k)*(V(:,1:k))';
    imshow(uint8(X2))
end
for k=1:1:60
    X3=U(:,1:k)*S(1:k,1:k)*(V(:,1:k))';
    imshow(uint8(X3))
end
for k=1:1:150
    X4=U(:,1:k)*S(1:k,1:k)*(V(:,1:k))';
    imshow(uint8(X4))
end
