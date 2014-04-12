# usage: multplicate.sh "ack creationTimeStamp"
#HH_PROJECTS="~/re"
#cd $HH_PROJECTS
for i in $( ls -l | egrep '^d' | awk '{print $8}' | head -10 ); do
    cd $i
    git fetch --quiet && git checkout origin/master --quiet && "$@" && git checkout - --quiet
    cd ..
done

#for project in ls
#
