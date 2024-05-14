#include "arch.h"
#include "ccbench.h"

// gcc  -I/home/vinhq/RELAX/ParallelProgramming/ccbench/include test.c arch.c x86.c generic.c properties.c -o test

static inline int cacheflush(int level,int num_flushes,int mode,void* buffer,cpu_info_t cpuinfo) {

  unsigned long long stride=cpuinfo.Cacheline_size[level-1]/num_flushes;
  unsigned long long size=0;
  int i,j,tmp=0x0fa38b09;

  if (level>cpuinfo.Cachelevels) return -1;

  // get cache size of each level
  // size = size of all caches up to level
  //exclusive caches
  if ((!strcmp(cpuinfo.vendor,"AuthenticAMD")) && (cpuinfo.family != 21))for (i=0;i<level;i++)
  {
     if (cpuinfo.Cache_unified[i]) size+=cpuinfo.U_Cache_Size[i];
     else size+=cpuinfo.D_Cache_Size[i];
  }
  //inclusive L2, exclusive L3
  if ((!strcmp(cpuinfo.vendor,"AuthenticAMD")) && (cpuinfo.family == 21))
  {
    if (level<3)
    {
      i=level-1;
   	  if (cpuinfo.Cache_unified[i]) size=cpuinfo.U_Cache_Size[i];
      else size=cpuinfo.D_Cache_Size[i];
    }
    else for (i=1;i<level;i++)
    {     
     if (cpuinfo.Cache_unified[i]) size+=cpuinfo.U_Cache_Size[i];
     else size+=cpuinfo.D_Cache_Size[i];
    }
  }
  //inclusive caches
  if (!strcmp(cpuinfo.vendor,"GenuineIntel"))
  {
     i=level-1;
     if (cpuinfo.Cache_unified[i]) size=cpuinfo.U_Cache_Size[i];
     else size=cpuinfo.D_Cache_Size[i];
  } 

  size*=cpuinfo.EXTRA_FLUSH_SIZE;
  // double amount of accessed memory for LLC flushes and decrease num_flushes
  if (level==cpuinfo.Cachelevels){ 
    size*=2;
    num_flushes/=3;
    num_flushes++;
  }
  size/=100;

  if (stride<sizeof(unsigned int)) stride=sizeof(unsigned int);
  
  if (mode!=MODE_RDONLY){
    j=num_flushes;
    while(j--)
    {
     for (i=0;i<size;i+=stride)
     {
       tmp|=*((int*)((unsigned long long)buffer+i));
       *((int*)((unsigned long long)buffer+i))=tmp;
     }
    }
  }
  if ((mode==MODE_EXCLUSIVE)||(mode==MODE_INVALID)){
    clflush(buffer,size,cpuinfo);
  }
  if ((mode==MODE_EXCLUSIVE)||(mode==MODE_RDONLY)){
    j=num_flushes;
    while(j--)
    {
     for (i=0;i<size;i+=stride)
     {
       tmp|=*((int*)((unsigned long long)buffer+i));
     }
     *((int*)((unsigned long long)buffer+i))=tmp;
    }
  }

  return tmp;

}

int main () {


  cpu_info_t cpu_info;
  init_cpuinfo(&cpu_info, 1);


  return 0;
}
