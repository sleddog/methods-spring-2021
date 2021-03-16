#!/bin/bash
read -p "Enter a number > " number
echo "you entered $number"

gcc solution.c -o solution 
./solution << EOF
$number
EOF

