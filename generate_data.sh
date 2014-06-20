# generate data 1 - 10

for i in {1..10}; do
    let j=i+1
    echo $i $j >> data1.txt
done
