if [[ $# < 1 ]]; then
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

echo "Running..."
# runnnig selected file or every file
if [[ $# == 2 ]]; then
  echo "Java file:" $2
  java $2
else
  for file in $java_files; do
    file_name=`echo $file | cut -d'.' -f1`
    echo "Java file:" $file_name
    java $file_name
  done
fi
