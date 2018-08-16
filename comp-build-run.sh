if [[ $# != 1 ]]; then
  echo "Usage: ./comp-build-run.sh <week-#>"
  exit
fi

# entering the folder passed
cd programming-exercises/$1
echo "Currently in..."
pwd

# getting java files
java_files=`ls | grep ".java"`

echo "Compiling..."
# compiling every file
for file in $java_files; do
  javac -cp "../../algs4.jar" $file
  echo $file "compiled!"
done
