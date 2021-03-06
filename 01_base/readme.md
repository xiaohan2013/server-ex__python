

### 进程

> 指正在处理任务或者正在进行中的程序。 
> 一个程序启动两次属于2个进程


### 协程


### 并发与并行

* 并发：单核条件下，正在运行中的多个程序，CPU被操作系统调度，对遇到I/O操作和运行时间足够长的程序进行切换，并且在切换过程中对上次执行的结果保存在操作系统内存中，以便CPU回切执行程序时从上次结束的位置继续。


* 并行： 多核条件下，每个CPU对应一个任务进行处理


### 同步与异步
- 同步

> 两个进程间的通信，好比两个人打电话，必须都在才行

- 异步

> 一个进程的数据发到第三方，另一个进程从第三方去获取。类似发短信，一个人发送短信到电信公司，由电信公司转交，但接收方不一定在，时间上不固定

### 进程的层次结构

- Linux系统

> 父进程和子进程的关系，子类会全部拷贝父类的初始状态，只限父子之间的拷贝，并且是初始状态

- Windows系统

>一个进程在执行过程中产生新的进程，没有继承父类的任何东西，并且是两个完全独立的进程


* [Python进程、线程、协程详解](http://blog.csdn.net/Saliva520319/article/details/52230405)


## Python并发
* threading： 编写多线程
* multiprocessing: 编写多进程
* ThreadPoolExecutor和ProcessPoolExecutor实现线程池和进程池的操作
* concurrent.fueatures提供了excutor和future来实现

## Python异步编程
* Future理解为未来完成的操作，这是异步的基础；
* wait方法返回一个元组。


## Python协程（微线程）
1. 协程，又叫微线程(Coroutine)
2. 子程序（子函数），在所有语言中都是层级调用，比如A调用B，B在执行过程中又调用了C，C执行完毕返回，B执行完毕返回，最后是A执行完毕。所以子程序调用是通过栈实现的，一个线程就是执行一个子程序;
3. 协程不同于线程，线程是抢占式的调度，而协程是协同式的调度，协程需要自己做调度。 
子程序调用总是一个入口，一次返回，调用顺序是明确的。而协程的调用和子程序不同。协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行;
4. 协程优势是极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。用来执行协程多任务非常合适;
5. 协程没有线程的安全问题。一个进程可以同时存在多个协程，但是只有一个协程是激活的，而且协程的激活和休眠又程序员通过编程来控制，而不是操作系统控制的。 
因为协程是一个线程中执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能;
6. Python对协程的支持是通过generator实现的。在generator中，我们不但可以通过for循环来迭代，还可以不断调用next()函数获取由yield语句返回的下一个值。但是Python的yield不但可以返回一个值，它还可以接收调用者发出的参数。


