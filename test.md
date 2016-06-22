前言 {#ch:preface}
====

<span><span>C++ Programming
Style</span></span>是一份关于<span><span>C++</span></span>的代码规范，为<span><span>C++</span></span>程序员提供程序设计的参考和建议。

规范总结了我们长期在编码实践中遇到的一些宝贵经验，其中部分规则、原则和建议摘自社区软件设计大师的论文、报告、书籍和博客，并引用了一些典型的源代码。

约定 {#约定 .unnumbered}
----

宏定义 {#宏定义 .unnumbered}
------

为了提高代码的表现力，规范中使用了一部分实用的宏定义。为了避免歧义，这里列出了部分较为重要的宏定义供参考和查阅。

\[caption=\] \#ifndef GKOQWPRT\_1038935\_NCVBNMZHJS\_8909603 \#define
GKOQWPRT\_1038935\_NCVBNMZHJS\_8909603

namespace details

template &lt;typename T&gt; struct DefaultValue <span> static T value()
<span> return T(); </span> </span>;

template &lt;typename T&gt; struct DefaultValue&lt;T\*&gt; <span> static
T\* value() <span> return 0; </span> </span>;

template &lt;typename T&gt; struct DefaultValue&lt;const T\*&gt; <span>
static T\* value() <span> return 0; </span> </span>;

template &lt;&gt; struct DefaultValue&lt;void&gt; <span> static void
value() <span> </span> </span>;

\#define DEFAULT(type, method) virtual type method <span> return
::details::DefaultValue&lt;type&gt;::value(); </span>

\#endif

<span><span>DEFAULT</span></span>对于定义空实现的<span><span>virtual</span></span>函数非常方便。需要注意的是，<span><span>DEFAULT</span></span>所有计算都是发生在编译时，并没有任何运行时成本。

\[caption=\] \#ifndef H16274882\_9153\_4DB2\_A2E2\_F23D4CCB9381 \#define
H16274882\_9153\_4DB2\_A2E2\_F23D4CCB9381

\#include &lt;cub/base/Config.h&gt; \#include &lt;cub/base/Default.h&gt;

\#define ABSTRACT(...) virtual \_\_VA\_ARGS\_\_ = 0

\#if \_\_SUPPORT\_VIRTUAL\_OVERRIDE \# define OVERRIDE(...) virtual
\_\_VA\_ARGS\_\_ override \#else \# define OVERRIDE(...) virtual
\_\_VA\_ARGS\_\_ \#endif

\#define EXTENDS(...) , \#\#\_\_VA\_ARGS\_\_ \#define IMPLEMENTS(...)
EXTENDS(\_\_VA\_ARGS\_\_)

\#endif

<span><span>Config.h</span></span>提供了编译器支持<span><span>C++11</span></span>特性的配置信息。<span><span>ABSTRACT,
OVERRIDE, EXTENDS,
IMPLEMENTS</span></span>等关键字，使得其他阵营的程序员，也能看懂规范中大部分<span><span>C++</span></span>的代码，极大地改善了<span><span>C++</span></span>的表现力。

\[caption=\] \#ifndef HF95EF112\_D6C6\_4DB0\_8C1A\_BE5A6CF8E3F1 \#define
HF95EF112\_D6C6\_4DB0\_8C1A\_BE5A6CF8E3F1

\#include &lt;cub/base/Keywords.h&gt;

namespace details <span> template &lt;typename T&gt; struct Role <span>
virtual  Role() </span>; </span>

\#define DEFINE\_ROLE(type) struct type : ::details::Role&lt;type&gt;

\#endif

通过<span><span>DEFINE\_ROLE</span></span>的宏定义来实现对接口的定义，可以消除子类对虚拟析构函数的重复实现，消除代码重复。

致谢 {#致谢 .unnumbered}
----

本规范主要由刘光聪(毕诚)编写，并由袁英杰审阅。此外，规范由<span><span>COCK(C++
Optimal Construction
Kit)</span></span>社区的组员长期维护和持续更新，感谢各位小伙伴们的积极参与。

由于时间的仓促，规范错误再所难免。如果您发现了错误，或者有更好的意见，请第一时间联系<span><span>COCK</span></span>的小伙伴，我们将非常感激！

\[45mm\] <span><span>Do the simplest thing that could possibly
work.</span></span>

代码风格 {#ch:physical-design}
========

开发环境
--------

系统中所有的代码看起来就好像是由单独一个值得胜任的人编写的。[^1]。

我们倡导<span><span>XP</span></span>的价值观，致力于优秀的软件设计。遵循统一的代码规范，可以使的团队内部形成统一的代码风格，降低沟通成本，增强系统的可理解性。

为了保证代码的最大可移植性，团队使用的操作系统、编译器类型、版本等基础设施应保持一致性，遵循统一的，一致的，没有歧义的代码规范。

不推荐在<span><span>Windows</span></span>上开发<span><span>C/C++</span></span>程序；推荐使用<span><span>Linux</span></span>，<span><span>MacOS</span></span>等类<span><span>Unix</span></span>操作系统。

团队统一使用相同的集成开发环境<span><span>(IDE)</span></span>，并使用统一的代码模板，保持代码风格的一致性。

推荐两款集成开发环境<span><span>(IDE)</span></span>，因为它们都支持良好的重构功能：

<span>*<span><span><span>Eclipse</span></span></span>*</span>

<span>*<span><span><span>Clion</span></span></span>*</span>

团队使用统一<span><span>IDE</span></span>的主题风格，例如代码模板。

团队应该建立统一的<span><span>IDE</span></span>的主题，团队成员可简单地导入主题，即可完成环境的自动配置，形成团队内部的统一规范。

团队统一配置<span><span>IDE</span></span>使用等宽字体

如果团队中有人使用非等宽字体，会造成团队内部代码对不齐、缩进混乱的情况。优秀的程序员在写第一行代码前，都会将自己的编译环境、颜色、字体等调整到最佳状态，以便在写代码的时候更友好地、更快捷地反馈所存在的问题，提高工作效率。

团队统一配置<span><span>IDE</span></span>的文件编码格式，避免中文出现乱码的现象

强烈推荐遵循良好的代码注释的规范和最佳实践；倡导整洁代码，代码自解释；即使在特殊场景需要注释时，应使用标准的英文注释。

团队统一配置<span><span>IDE</span></span>的<span><span>TAB</span></span>为相同数目的空格，坚决抵制使用<span><span>TAB</span></span>对齐代码[^2]

因各种编辑器解释<span><span>TAB</span></span>的长度存在不一致，如果使用<span><span>TAB</span></span>对齐代码，可能会使代码缩进混乱不堪。

代码风格 {#代码风格}
--------

团队应该保持一致的命名、缩进、空格、空行、断行的代码风格。

业界存在多种经典的代码风格，各自都拥有独特的优势，团队应该选择并保持其中一种代码风格。

<span>*<span><span><span>K&R</span></span></span>*</span>

<span>*<span><span><span>BSD/Allman</span></span></span>*</span>

<span>*<span><span><span>GNU</span></span></span>*</span>

<span>*<span><span><span>Whitesmiths</span></span></span>*</span>

统一代码风格并非难事，团队发布统一的<span><span>IDE</span></span>代码模板，及其定制一个方便的格式化快捷键即可解决所有对齐、缩进、空格、断行等问题。

程序实体之间有且仅有一行空行。

函数之间的空行，能够帮组我们快速定位函数的始末的准确位置；甚至在函数内部，将逻辑相关的代码放在一起也同样具有意义（理论应该提取该函数，并合理命名），它能够帮助我们更好地理解代码块的语义。

超过一行的空行完全没有必要，部分粗心的程序员在处理这些细节时总存在着或多或少的问题，团队应该杜绝这样的情况发生。

每个文件末尾都应该有且仅有一行空行。

如果使用<span><span>Eclipse</span></span>，在创建新文件时自动地在文件末添加一行空行；但诸如<span><span>Visual
C++</span></span>等情况下，则需要程序员在文件末自行手动地添加一行空行。这样做可以最大化地实现代码的可移植性，避免某些编译器因缺少空行而产生警告信息。

每一行的代码或注释不得超过<span><span>80</span></span>列；否则将其拆分为若干行，并保持适当缩进，保证排版整洁漂亮。

长表达式、长语句或多或少都存在重复，此时往往是函数提取、概念整合的最佳时机，缩短长表达式、长语句可以极大地改善代码的可读性，缩短代码阅读和理解的时间。

注释符号与注释内容之间要用一个空格分割

当注释内容与注释符号之间没有空格，尤其是中文注释，导致部分编译器词法分析错误，导致编译失败。

反例：

/\*multi-line comment\*/ //sigle-line comment

正例：

/\* multi-line comment \*/ // single-line comment

\[45mm\] <span><span>Any fool can write code that a computer can
understand. Good programmers write code that humans can
understand.</span></span>

物理设计 {#ch:physical-design}
========

概念
----

物理设计主要是软件设计中的物理实体（文件）的设计，例如某个函数定义应该放在哪个文件中、某个函数是否需要<span><span>inline</span></span>等；逻辑设计主要针对软件设计中的逻辑实体关系的设计，例如类之间的关系，<span><span>has-a/use-a/is-a</span></span>的关系。

物理设计的主要目标是减少文件的物理依赖；而逻辑设计的主要目标是减少逻辑依赖。物理依赖更多的体现为编译时的依赖和链接时的依赖；物理依赖受逻辑依赖影响，但是又不局限于逻辑依赖。

物理结构
--------

遵循惯例优于配置的基本原则，公司内部所有项目组织结构应该保持一致，便于项目的自动化构建。

以<span><span>cut</span></span>项目为例，总体上分<span><span>include,
src,
test</span></span>三个目录；头文件，源文件，测试文件存在对称关系；构建文件分级构建，例如‘CMakeLists.txt,
Makefile‘。

正例：

\[caption=<span>项目结构</span>\] cut ├── CMakeLists.txt ├── LICENSE ├──
README.md ├── include │   └── cut │   ├── core │   │   ├── Test.h │  
│   ├── TestCase.h │   │   ├── TestFixture.h │   │   ├── TestListener.h
│   │   ├── TestResult.h │   │   ├── TestRunner.h │   │   └──
TestSuite.h │   ├── cut.h │   ├── cut.hpp ├── src │   ├── CMakeLists.txt
│   └── cut │   ├── core │   │   ├── TestCase.cpp │   │   ├──
TestResult.cpp │   │   ├── TestRunner.cpp │   │   └── TestSuite.cpp └──
test ├── CMakeLists.txt ├── cut │   ├── TestCaseSpec.cpp │   ├──
TestSuiteSpec.cpp │   ├── TestListenerSpec.cpp ├── main.cpp

文件布局，团队应遵循统一的风格。

一个头文件包括头文件保护宏，<span><span>include</span></span>语句，命名空间，前置声明，类定义等。

正例：

\[caption=\] \#ifndef
\_YILL50M2RW1ONKOTDE31GYE4PZNVDLHH1CKFXS75LL4DA2NDCQSX9H5Y \#define
\_YILL50M2RW1ONKOTDE31GYE4PZNVDLHH1CKFXS75LL4DA2NDCQSX9H5Y

\#include &lt;cut/core/Test.h&gt; \#include
&lt;cut/core/TestFixture.h&gt;

CUT\_NS\_BEGIN

struct TestCase : Test, TestFixture

TestCase(const std::string& name);

void runBare(TestResult&);

private: OVERRIDE(void run(TestResult&)); OVERRIDE(int countTestCases()
const); OVERRIDE(int countChildTests() const); OVERRIDE(const
std::string& getName() const);

private: DEFAULT(void, runTest());

private: template &lt;typename Functor&gt; bool protect(TestResult&
result, Functor functor, const char\* desc = “”);

private: const std::string name;

;

CUT\_NS\_END

\#endif

实现文件的布局，包括匿名命名空间定义，类成员函数实现等等。

正例：

\[caption=\] \#include &lt;cut/core/TestCase.h&gt; \#include
&lt;cut/core/TestFunctor.h&gt; \#include &lt;cut/core/TestResult.h&gt;

CUT\_NS\_BEGIN

TestCase::TestCase(const std::string& name) : name(name)

namespace

struct TestCaseFunctor : TestFunctor

using Method = void(TestCase::\*)();

TestCaseFunctor(TestCase& test, Method method) : test(test),
method(method)

private: OVERRIDE(bool operator()() const) <span> (test.\*method)();
return true; </span>

IMPL\_ROLE\_WITH\_OBJ(Test, test);

private: TestCase& test; Method method;

;

template &lt;typename Functor&gt; inline bool
TestCase::protect(TestResult& result, Functor functor, const char\*
desc) <span> return result.protect(TestCaseFunctor(\*this, functor),
desc); </span>

\#define PROTECT(functor) protect(result, &TestCase::functor, “ in the
”\#functor)

void TestCase::runBare(TestResult& result) <span> if (PROTECT(setUp))
<span> PROTECT(runTest); </span> PROTECT(tearDown); </span>

void TestCase::run(TestResult& result) <span> result.run(\*this);
</span>

int TestCase::countTestCases() const <span> return 1; </span>

int TestCase::countChildTests() const <span> return 0; </span>

const std::string& TestCase::getName() const <span> return name; </span>

CUT\_NS\_END

实现文件是一种典型的隐藏实现的技术，能够极大地缩小用户依赖的范围，为此我们鼓励实现的隐藏和封装。例如，<span><span>TestCase::protect</span></span>虽然是模板，但它仅仅被<span><span>TestCase::runBare</span></span>所范围，为此在头文件中将其声明为<span><span>private</span></span>，并且没有在头文件中展开实现。

\[caption=\] struct TestCase : Test, TestFixture

...

private: template &lt;typename Functor&gt; bool protect(TestResult&
result, Functor functor, const char\* desc = “”);

;

而只需在实现文件中，在被依赖的点之前完成模板的定义即可；并且在定义时，因为在实现文件内部，所以可以大胆地使用<span><span>inline</span></span>机制。

\[caption=\] template &lt;typename Functor&gt; inline bool
TestCase::protect(TestResult& result, Functor functor, const char\*
desc) <span> return result.protect(TestCaseFunctor(\*this, functor),
desc); </span>

\#define PROTECT(functor) protect(result, &TestCase::functor, “ in the
”\#functor)

void TestCase::runBare(TestResult& result) <span> if (PROTECT(setUp))
<span> PROTECT(runTest); </span> PROTECT(tearDown); </span>

头文件
------

自定义头文件必须具有扩展名，以区分<span><span>C++</span></span>标准库的头文件；在团队内部，头文件、源文件扩展名类型必须保持一致性。

表<span><span>*<span>表</span><span><span>\[tbl:file-extension\]（第页）</span></span>*</span></span>列出了头文件和实现文件常见的扩展名，团队应该选择一类扩展名并保持团队内一致性。

每一个头文件都应该具有独一无二的保护宏，并保持命名规则的一致性

命名规则包括两种风格：

<span>*<span>INCL\_&lt;PROJECT&gt;\_&lt;MODULE&gt;\_&lt;FILE&gt;\_H</span>*</span>

<span>*<span><span><span>全局唯一的随机序列码[^3]</span></span></span>*</span>

第一种命名规则问题在于：当文件名重命名或移动目录时，需要同步修改头文件保护宏；推荐使用<span><span>IDE</span></span>随机自动地生成头文件保护宏，其更加快捷、简单、安全、有效。

反例：

\[caption=\] // 因名称太短，存在名字冲突的可能性 \#ifndef RUNNABLE\_H
\#define RUNNABLE\_H

\#include &lt;cub/base/Role.h&gt;

DEFINE\_ROLE(Runnable) <span> ABSTRACT(void run()); </span>;

\#endif

正例：

\[caption=\] // UUID: IDE自动生成 \#ifndef
ADCM\_LLL\_3465\_DCPOE\_ACLDDDE\_479\_YTEY\_SDJWEOX\_234798SDN \#define
ADCM\_LLL\_3465\_DCPOE\_ACLDDDE\_479\_YTEY\_SDJWEOX\_234798SDN

\#include &lt;cub/base/Role.h&gt;

DEFINE\_ROLE(Runnable) <span> ABSTRACT(void run()); </span>;

\#endif

包含头文件时，统一使用尖括号。

即使在同一目录下，也不采用相对路径包含头文件。这样做，在没有严重牺牲编译效率的前提下，可以形成同一的代码规范，程序员再也不用被这件事情所困扰。

反例：

\[caption=\] \#ifndef
\_YILL50M2RW1ONKOTDE31GYE4PZNVDLHH1CKFXS75LL4DA2NDCQSX9H5Y \#define
\_YILL50M2RW1ONKOTDE31GYE4PZNVDLHH1CKFXS75LL4DA2NDCQSX9H5Y

// 即使TestCase, Test, TestFixture在同一目录， //
也不采用相对路径的方式组织include语句 \#include “Test.h” \#include
“TestFixture.h”

CUT\_NS\_BEGIN

struct TestCase : Test, TestFixture

TestCase(const std::string& name);

private: OVERRIDE(void run(TestResult&)); OVERRIDE(int countTestCases()
const); OVERRIDE(int countChildTests() const); OVERRIDE(const
std::string& getName() const);

private: const std::string name;

;

CUT\_NS\_END

\#endif

正例：

\[caption=\] \#ifndef
\_YILL50M2RW1ONKOTDE31GYE4PZNVDLHH1CKFXS75LL4DA2NDCQSX9H5Y \#define
\_YILL50M2RW1ONKOTDE31GYE4PZNVDLHH1CKFXS75LL4DA2NDCQSX9H5Y

// 统一采用：\#include &lt;project/module/file.h&gt;的风格 \#include
&lt;cut/core/Test.h&gt; \#include &lt;cut/core/TestFixture.h&gt;

CUT\_NS\_BEGIN

struct TestCase : Test, TestFixture

TestCase(const std::string& name);

private: OVERRIDE(void run(TestResult&)); OVERRIDE(int countTestCases()
const); OVERRIDE(int countChildTests() const); OVERRIDE(const
std::string& getName() const);

private: const std::string name;

;

CUT\_NS\_END

\#endif

文件名应该与程序主要实体名称相同。

反例：

\[caption=\] // 文件名与类名不一致 struct TestCase

explicit TestCase(const std::string& name);

private: const std::string name;

;

正例：

\[caption=\] struct TestCase

explicit TestCase(const std::string& name);

private: const std::string name;

;

路径名一律使用小写、下划线或中划线风格的名称。

反例：

\[caption=<span>驼峰风格的路径名</span>\] //
路径名<span><span>htmlParser</span></span>使用了驼峰命名风格 \#include
&lt;htmlParser/core/Attribute.h&gt;

正例：

\[caption=<span>正确的头文件包含</span>\] \#include
&lt;html-parser/core/Attribute.h&gt;

包含头文件时，必须保持路径名、文件名大小写敏感

为了保证代码的最大化可移植性，在包含头文件时必须保持文件名的大小写敏感。

假如存在两个物理文件名，真实的路径分别为：<span><span>cub/base/SynchronizedObject.h,
ymal/yaml\_parser.h</span></span>。

反例：

// 路径名大小写与真实物理路径不符 \#include
&lt;Cub/Base/SynchronizedObject.h&gt;

// 文件名大小写与真实物理文件名称不符 \#include
&lt;ymal/YAML\_Parser.h&gt;

正例：

\#include &lt;cut/core/SynchronizedObject.h&gt; \#include
&lt;yaml\_parser.h&gt;

包含头文件时，路径分隔符一律使用<span><span>Unix</span></span>风格，拒绝使用<span><span>Windows</span></span>风格。

反例：

// 使用了Windows风格的路径分割符 \#include &lt;cub.h&gt;

正例：

// 使用了Unix风格的路径分割符 \#include
&lt;cub/base/SynchronizedObject.h&gt;

使用<span><span>extern</span></span>
`"`<span><span>C</span></span>`"`时，不要包括<span><span>include</span></span>语句

反例：

\[caption=\] \#ifndef HF0916DFB\_1CD1\_4811\_B82B\_9B8EB1A007D8 \#define
HF0916DFB\_1CD1\_4811\_B82B\_9B8EB1A007D8

\#ifdef \_\_cplusplus extern “C”

\#endif

// 错误地将include放在了extern “C”中 \#include &lt;oss\_def.h&gt;

void\* oss\_alloc(size\_t); void oss\_free(void\*);

\#ifdef \_\_cplusplus

\#endif

\#endif

正例：

\[caption=\] \#ifndef HF0916DFB\_1CD1\_4811\_B82B\_9B8EB1A007D8 \#define
HF0916DFB\_1CD1\_4811\_B82B\_9B8EB1A007D8

\#include &lt;oss/def.h&gt;

\#ifdef \_\_cplusplus extern “C”

\#endif

void\* oss\_alloc(size\_t); void oss\_free(void\*);

\#ifdef \_\_cplusplus

\#endif

\#endif

当以<span><span>C</span></span>提供实现时，头文件中必须使用<span><span>extern</span></span>
`"`<span><span>C</span></span>`"`声明，以便支持<span><span>C++</span></span>的扩展。

反例：

\[caption=<span>oss/oss\_memery.h</span>\] \#ifndef
HF0916DFB\_1CD1\_4811\_B82B\_9B8EB1A007D8 \#define
HF0916DFB\_1CD1\_4811\_B82B\_9B8EB1A007D8

\#include &lt;oss/def.h&gt;

void\* oss\_alloc(size\_t); void oss\_free(void\*);

\#endif

正例：

\[caption=<span>oss/oss\_memery.h</span>\] \#ifndef
HF0916DFB\_1CD1\_4811\_B82B\_9B8EB1A007D8 \#define
HF0916DFB\_1CD1\_4811\_B82B\_9B8EB1A007D8

\#include &lt;oss/def.h&gt;

\#ifdef \_\_cplusplus extern “C”

\#endif

void\* oss\_alloc(size\_t); void oss\_free(void\*);

\#ifdef \_\_cplusplus

\#endif

\#endif

拒绝创建巨型头文件，将所有实体声明都放到头文件中

不要把所有的宏、<span><span>const</span></span>常量、函数声明、类定义都要放在头文件中，而仅仅将外部依赖的实体声明放到头文件中。

实现文件也是一种信息隐藏的惯用技术，如果一些程序的实体不对外所依赖，则放在自己的实现文件中，一则可降低依赖关系，二则实现更好的信息隐藏。

巨型头文件必然造成了巨大的编译时依赖，不仅仅带来巨大的编译时开销，更重要的是这样的设计将太多的实现细节暴露给用户，导致后续版本兼容性的问题，阻碍了头文件进一步演进、修改、扩展的可能性，从而失去了软件的可扩展性。

不要认为提供一个大而全的头文件会给你的用户带来方便，用户因此而更加困扰。另外，头文件应该自满足，而不是让用户还要关心头文件之间的依赖关系。巨大的头文件，因为复杂，是很难保证其自满足性，从而带来维护上的麻烦，并且降低了代码的可读性。

物理设计原则
------------

物理设计是<span><span><span>C</span></span></span><span><span>/</span></span><span><span><span>C++</span></span></span>语言中特有的一部分，遵循<span><span>*<span>表</span><span><span>\[tbl:phyical-design-priciples\]（第页）</span></span>*</span></span>中所列的设计原则，必然可以得到更加清晰、更加漂亮的头文件设计。

自满足原则

所有头文件都应该自满足的。所谓头文件自满足，即头文件自身是可编译成功的。

看一个具体的示例代码，这里定义了一个<span><span>TestCase.h</span></span>头文件。<span><span>TestCase</span></span>对父类<span><span>TestLeaf,
TestFixture</span></span>都存在编译时依赖，但没有包含基类的头文件。

反例：

\[caption=\] \#ifndef EOPTIAWE\_23908576823\_MSLKJDFE\_0567925 \#define
EOPTIAWE\_23908576823\_MSLKJDFE\_0567925

struct TestCase : TestLeaf, TestFixture

TestCase(const std::string &name=“”);

private: OVERRIDE(void run(TestResult \*result)); OVERRIDE(std::string
getName() const);

private: ABSTRACT(void runTest());

private: const std::string name;

;

\#endif

为了满足自满足原则，其自身必须包含其所有父类的头文件。

正例：

\[caption=\] \#ifndef EOPTIAWE\_23908576823\_MSLKJDFE\_0567925 \#define
EOPTIAWE\_23908576823\_MSLKJDFE\_0567925

\#include &lt;cut/core/TestLeaf.h&gt; \#include
&lt;cut/core/TestFixture.h&gt;

struct TestCase : TestLeaf, TestFixture

TestCase(const std::string &name=“”);

private: OVERRIDE(void run(TestResult &result)); OVERRIDE(std::string
getName() const);

private: ABSTRACT(void runTest());

private: const std::string name;

;

\#endif

即使<span><span>TestCase</span></span>持有<span><span>std::string
name</span></span>成员变量，但没有必要包含<span><span>std::string</span></span>的头文件。因为<span><span>TestCase</span></span>覆写了其父类的<span><span>getName</span></span>成员函数，父类为了保证自满足原则，自然已经包含了<span><span>std::string</span></span>的头文件。

同样的原因，也没有必要在此前置声明<span><span>TestResult</span></span>，因为父类已经声明过了。两者成立的前提时，父类都要遵循良好的头文件自满足原则。

实现文件的第一行代码必然是包含其对应的头文件。

创建对应的实现文件<span><span>TestCase.cpp</span></span>，并将自身头文件的进行包含，并置在实现文件的第一行，这是验证头文件自满足的最好的办法。

反例：

\[caption=\] \#include &lt;cut/core/TestResult.h&gt; \#include
&lt;cut/core/Functor.h&gt; // 没有放在第一行，无法校验其自满足性
\#include &lt;cut/core/TestCase.h&gt;

namespace

struct TestCaseMethodFunctor : Functor

typedef void (TestCase::\*Method)();

TestCaseMethodFunctor(TestCase &target, Method method) : target(target),
method(method)

bool operator()() const <span> target.\*method(); return true; </span>

private: TestCase &target; Method method;

;

template &lt;typename Functor&gt; inline bool
TestCase::protect(TestResult& result, Functor functor, const char\*
desc) <span> return result.protect(TestCaseFunctor(\*this, functor),
desc); </span>

\#define PROTECT(functor) protect(result, &TestCase::functor, “ in the
”\#functor)

void TestCase::runBare(TestResult& result) <span> if (PROTECT(setUp))
<span> PROTECT(runTest); </span> PROTECT(tearDown); </span> ...

正例：

\[caption=\] \#include &lt;cut/core/TestCase.h&gt; \#include
&lt;cut/core/TestResult.h&gt; \#include &lt;cut/core/Functor.h&gt;

namespace

struct TestCaseMethodFunctor : Functor

typedef void (TestCase::\*Method)();

TestCaseMethodFunctor(TestCase &target, Method method) : target(target),
method(method)

bool operator()() const <span> target.\*method(); return true; </span>

private: TestCase &target; Method method;

;

\#define PROTECT(functor) protect(result, &TestCase::functor, “ in the
”\#functor)

void TestCase::runBare(TestResult& result) <span> if (PROTECT(setUp))
<span> PROTECT(runTest); </span> PROTECT(tearDown); </span>

...

单一职责

这是<span><span>SRP(Single Reponsibility
Priciple)</span></span>在头文件设计时的一个具体运用。头文件如果包含了其它不相关的元素，则包含该头文件的所有实现文件都将被这些不相关的元素所污染，重编译将成为一件高概率的事件。

如示例代码，将<span><span>OutputStream,
InputStream</span></span>同时定义在一个头文件中，将违背该原则。假如用户只需要只读接口，无意中地使得用户被只写接口所间接污染。

反例：

\[caption=\] \#ifndef LDGOUIETA\_437689Q20\_ASIOHKFGP\_980341 \#define
LDGOUIETA\_437689Q20\_ASIOHKFGP\_980341

\#include &lt;cut/base/Role.h&gt;

DEFINE\_ROLE(OutputStream) <span> ABSTRACT(void write()); </span>;

DEFINE\_ROLE(InputStream) <span> ABSTRACT(void read()); </span>;

\#endif

正例：先创建一个<span><span>OutputStream.h</span></span>文件：

\[caption=\] \#ifndef LDGOUIETA\_437689Q20\_ASIOHKFGP\_010234 \#define
LDGOUIETA\_437689Q20\_ASIOHKFGP\_010234

\#include &lt;cut/base/Role.h&gt;

DEFINE\_ROLE(OutputStream) <span> ABSTRACT(void write()); </span>;

\#endif

再创建一个<span><span>InputStream.h</span></span>文件：

\[caption=\] \#ifndef LDGOUIETA\_437689Q20\_ASIOHKFGP\_783621 \#define
LDGOUIETA\_437689Q20\_ASIOHKFGP\_783621

\#include &lt;cut/base/Role.h&gt;

DEFINE\_ROLE(InputStream) <span> ABSTRACT(void read()); </span>;

\#endif

最小依赖

一个头文件只应该包含必要的实体，尤其在头文件中仅仅对实体的声明产生依赖，那么前置声明是一种有效的降低编译时依赖的技术。

反例：

\[caption=\] \#ifndef PERTP\_8792346\_QQPKSKJ\_09472\_HAKHKAIE \#define
PERTP\_8792346\_QQPKSKJ\_09472\_HAKHKAIE

\#include &lt;cut/base/Role.h&gt; \#include
&lt;cut/core/TestResult.h&gt; \#include &lt;string&gt;

DEFINE\_ROLE(Test) <span> ABSTRACT(void run(TestResult& result));
ABSTRACT(int countTestCases() const); ABSTRACT(int getChildTestCount()
const); ABSTRACT(std::string getName() const); </span>;

\#endif

如示例代码，定义了一个<span><span>xUnit</span></span>框架中的<span><span>Test</span></span>顶级接口，其对<span><span>TestResult</span></span>的依赖仅仅是一个声明依赖，并没有必要包含<span><span>TestResult.h</span></span>，前置声明是解开这类编译依赖的钥匙。

值得注意的是，对标准库<span><span>std::string</span></span>的依赖，即使它仅作为返回值，但因为它实际上是一个<span><span>typedef</span></span>，所以必须老实地包含其对应的头文件。事实上，如果产生了对标准库名称的依赖，都需要包含对应的头文件。

另外，对<span><span>DEFINE\_ROLE</span></span>宏定义的依赖则需要包含相应的头文件，以便实现该头文件的自满足。

但是，<span><span>TestResult</span></span>仅作为成员函数的参数出现在头文件中，所以对<span><span>TestResult</span></span>的依赖只需前置声明即可。

正例：

\[caption=\] \#ifndef PERTP\_8792346\_QQPKSKJ\_09472\_HAKHKAIE \#define
PERTP\_8792346\_QQPKSKJ\_09472\_HAKHKAIE

\#include &lt;cut/base/Role.h&gt; \#include &lt;string&gt;

struct TestResult;

DEFINE\_ROLE(Test) <span> ABSTRACT(void run(TestResult& result));
ABSTRACT(int countTestCases() const); ABSTRACT(int getChildTestCount()
const); ABSTRACT(std::string getName() const); </span>;

\#endif

在选择包含头文件还是前置声明时，很多程序员感到迷茫。其实规则很简单，在如下场景前置声明即可，无需包含头文件：

<span>*<span><span><span>指针</span></span></span>*</span>

<span>*<span><span><span>引用</span></span></span>*</span>

<span>*<span><span><span>返回值</span></span></span>*</span>

<span>*<span><span><span>函数参数</span></span></span>*</span>

相反地，如果编译器需要知道实体的真正内容时，则必须包含头文件，此依赖也常常称为强编译时依赖。强编译时依赖主要包括如下几种场景：

<span>*<span><span><span>typedef</span></span>定义的实体[^4]</span>*</span>

<span>*<span><span><span>继承</span></span></span>*</span>

<span>*<span><span><span>宏</span></span></span>*</span>

<span>*<span><span><span>inline</span></span></span>*</span>

<span>*<span><span><span>template</span></span></span>*</span>

<span>*<span><span><span>引用类内部成员时</span></span></span>*</span>

<span>*<span>执行<span><span>sizeof</span></span>运算</span>*</span>

最小可见性

在头文件中定义一个类时，清晰、准确的<span><span>public, protected,
private</span></span>是传递设计意图的指示灯。其中<span><span>private</span></span>做为一种实现细节被隐藏起来，为适应未来不明确的变化提供便利的措施。

不要将所有的实体都<span><span>public</span></span>，这无疑是一种自杀式做法。应该以一种相反的习惯性思维，尽最大可能性将所有实体<span><span>private</span></span>，直到你被迫不得不这么做为止，依次放开可见性的权限。

如下例代码所示，按照<span><span>public-private,
function-data</span></span>依次排列类的成员，并对具有相同特征的成员归类，将大大改善类的整体布局，给读者留下清晰的设计意图。

反例：

\[caption=\] \#ifndef IUOTIOUQW\_NMAKLKLG\_984592\_KJSDKLJFLK \#define
IUOTIOUQW\_NMAKLKLG\_984592\_KJSDKLJFLK

\#include &lt;trans-dsl/action/Action.h&gt; \#include
&lt;trans-dsl/utils/EventHandlerRegistry.h&gt;

struct SimpleAsyncAction : Action

template&lt;typename T&gt; Status waitOn(const EventId eventId, T\*
thisPointer, Status (T::\*handler)(const TransactionInfo&, const
Event&), bool forever = false) <span> return
registry.addHandler(eventId, thisPointer, handler, forever); </span>

Status waitUntouchEvent(const EventId eventId);

OVERRIDE(Status handleEvent(const TransactionInfo&, const Event&));
OVERRIDE(void kill(const TransactionInfo&, const Status));

DEFAULT(void, doKill(const TransactionInfo&, const Status));

EventHandlerRegistry registry;

;

\#endif

正例：

\[caption=\] \#ifndef IUOTIOUQW\_NMAKLKLG\_984592\_KJSDKLJFLK \#define
IUOTIOUQW\_NMAKLKLG\_984592\_KJSDKLJFLK

\#include &lt;trans-dsl/action/Action.h&gt; \#include
&lt;trans-dsl/utils/EventHandlerRegistry.h&gt;

struct SimpleAsyncAction : Action

template&lt;typename T&gt; Status waitOn(const EventId eventId, T\*
thisPointer, Status (T::\*handler)(const TransactionInfo&, const
Event&), bool forever = false) <span> return
registry.addHandler(eventId, thisPointer, handler, forever); </span>

Status waitUntouchEvent(const EventId eventId);

private: OVERRIDE(Status handleEvent(const TransactionInfo&, const
Event&)); OVERRIDE(void kill(const TransactionInfo&, const Status));

private: DEFAULT(void, doKill(const TransactionInfo&, const Status));

private: EventHandlerRegistry registry;

;

\#endif

所有<span><span>override</span></span>的函数[^5]都应该是<span><span>private</span></span>的，以保证用户遵循按照接口编程的良好设计原则。

反例：

\[caption=\] \#ifndef EOIPWORPIO\_06123124\_NMVBNSDHJF\_497392 \#define
EOIPWORPIO\_06123124\_NMVBNSDHJF\_497392

\#include &lt;html-parser/filter/NodeFilter.h&gt; \#include &lt;list&gt;

struct AndFilter : NodeFilter

void add(NodeFilter\*);

// 错误：本应该private OVERRIDE(bool accept(const Node&) const);

private: std::list&lt;NodeFilter\*&gt; filters;

;

\#endif

正例：

\[caption=\] \#ifndef EOIPWORPIO\_06123124\_NMVBNSDHJF\_497392 \#define
EOIPWORPIO\_06123124\_NMVBNSDHJF\_497392

\#include &lt;html-parser/filter/NodeFilter.h&gt; \#include &lt;list&gt;

struct AndFilter : NodeFilter

void add(NodeFilter\*);

private: OVERRIDE(bool accept(const Node&) const);

private: std::list&lt;NodeFilter\*&gt; filters;

;

\#endif

Inline
------

头文件中避免定义<span><span>inline</span></span>函数，除非性能报告指出此函数是性能的关键瓶颈

<span><span><span>C++</span></span></span>语言将声明和实现进行分离，程序员为此不得不在头文件和实现文件中重复地对函数进行声明。这是一件痛苦的事情，驱使部分程序员直接将函数实现为<span><span>inline</span></span>。

但<span><span>inline</span></span>函数的代码作为一种不稳定的内部实现细节，被放置在头文件里，
其变更所导致的大面积的重新编译是个大概率事件，为改善微乎其微的函数调用性能与其相比将得不偿失。除非有相关<span><span>profiling</span></span>性能测试报告，表明这部分关键的热点代码需要被放回头文件中。

让我们就像容忍头文件中宏保护符那样，也慢慢习惯<span><span><span>C</span></span></span>/<span><span><span>C++</span></span></span>天生给我们带来的这点点重复吧。

但需要注意，有两类特殊的情况，可以将实现<span><span>inline</span></span>在头文件中，因为为它们创建实现文件过于累赘和麻烦。

<span>*<span><span><span>virtual析构函数</span></span></span>*</span>

<span>*<span><span><span>空的virtual函数实现</span></span></span>*</span>

<span>*<span><span><span>11的default函数</span></span></span>*</span>

实现文件中鼓励<span><span>inline</span></span>函数实现

对于在编译单元内部定义的类而言，因为它的客户数量是确定的，就是它本身。另外，由于它本来就定义在源代码文件中，因此并没有增加任何“物理耦合”。所以，对于这样的类，我们大可以将其所有函数都实现为<span><span>inline</span></span>的，就像写<span><span>Java</span></span>代码那样，<span><span>Once
& Only Once</span></span>。

以单态类的一种实现技术为例，讲解编译时依赖的解耦与匿名命名空间的使用。(首先，应该抵制单态设计的诱惑，单态其本质是面向对象技术中全局变量的替代品。滥用单态模式，犹如滥用全局变量，是一种典型的设计坏味道。只有确定在系统中唯一存在的概念，才能使用单态模式)。

实现单态，需要对系统中唯一存在的概念进行封装；但这个概念往往具有巨大的数据结构，如果将其声明在头文件中，无疑造成很大的编译时依赖。

反例：

\[caption=\] \#ifndef UIJVASDF\_8945873\_YUQWTYRDF\_85643 \#define
UIJVASDF\_8945873\_YUQWTYRDF\_85643

\#include &lt;cut/base/Status.h&gt; \#include
&lt;cut/base/BaseTypes.h&gt; \#include
&lt;transport/ne/NetworkElement.h&gt; \#include &lt;vector&gt;

struct NetworkElementRepository

static NetworkElement& getInstance();

Status add(const U16 id); Status release(const U16 id); Status
modify(const U16 id);

private: typedef std::vector&lt;NetworkElement&gt; NetworkElements;
NetworkElements elements;

;

\#endif

受文章篇幅的所限，<span><span>NetworkElement.h</span></span>未列出所有代码实现，但我们知道<span><span>NetworkElement</span></span>拥有巨大的数据结构，上述设计导致所有包含<span><span>NetworkElementRepository</span></span>的头文件都被<span><span>NetworkElement</span></span>所间接污染。

此时，其中可以将依赖置入到实现文件中，解除揭开其严重的编译时依赖。更重要的是，它更好地遵守了按接口编程的原则，改善了软件的扩展性。

正例：

\[caption=\] \#ifndef UIJVASDF\_8945873\_YUQWTYRDF\_85643 \#define
UIJVASDF\_8945873\_YUQWTYRDF\_85643

\#include &lt;cut/base/Status.h&gt; \#include
&lt;cut/base/BaseTypes.h&gt; \#include &lt;cut/base/Role.h&gt;

DEFINE\_ROLE(NetworkElementRepository)

static NetworkElementRepository& getInstance();

ABSTRACT(Status add(const U16 id)); ABSTRACT(Status release(const U16
id)); ABSTRACT(Status modify(const U16 id));

;

\#endif

其实现文件包含<span><span>NetworkElement.h</span></span>，将对其的依赖控制在本编译单元内部。

\[caption=\]

\#include &lt;transport/ne/NetworkElementRepository.h&gt; \#include
&lt;transport/ne/NetworkElement.h&gt; \#include &lt;vector&gt;

namespace

struct NetworkElementRepositoryImpl : NetworkElementRepository

OVERRIDE(Status add(const U16 id)) <span> // inline implements </span>

OVERRIDE(Status release(const U16 id)) <span> // inline implements
</span>

OVERRIDE(Status modify(const U16 id)) <span> // inline implements
</span>

private: typedef std::vector&lt;NetworkElement&gt; NetworkElements;
NetworkElements elements;

;

NetworkElementRepository& NetworkElementRepository::getInstance() <span>
static NetworkElementRepositoryImpl inst; return inst; </span>

此处，对<span><span>NetworkElementRepositoryImpl</span></span>类的依赖是非常明确的，仅本编译单元内，所有可以直接进行<span><span>inline</span></span>，从而简化了很多实现[^6]。

实现文件中提倡使用匿名<span><span>namespace</span></span>,
以避免命名冲突。

匿名<span><span>namespace</span></span>的存在常常被人遗忘，但它的确是一个利器。匿名<span><span>namespace</span></span>的存在，使得所有受限于编译单元内的实体拥有了明确的处所。

自此之后，所有<span><span><span>C</span></span></span>风格，并局限于编译单元内的<span><span>static</span></span>函数和变量；以及类似<span><span>Java</span></span>中常见的<span><span>private
static</span></span>的提取函数将常常被匿名<span><span>namespace</span></span>替代。请记住匿名命名空间也是一种重要的信息隐藏技术。

struct VS. class
----------------

在类定义时，建议统一使用<span><span>struct</span></span>；但绝不允许<span><span>struct,
class</span></span>。

除了名字不同之外，<span><span>class</span></span>和<span><span>struct</span></span>唯一的差别是：默认可见性。这体现在定义和继承时。<span><span>struct</span></span>在定义一个成员，或者继承时，如果不指明，则默认为<span><span>public</span></span>，而<span><span>class</span></span>则默认为<span><span>private</span></span>。

但这些都不是重点，重点在于定义接口和继承时，冗余<span><span>public</span></span>修饰符总让人不舒服。简单设计四原则告诉告诉我们，所有冗余的代码都应该被剔除。

\[caption=\] \#ifndef OIWER\_NMVCHJKSD\_TYT\_48457\_GSDFUIE \#define
OIWER\_NMVCHJKSD\_TYT\_48457\_GSDFUIE

struct Description;

struct SelfDescribing <span> virtual void describeTo(Description&
description) const = 0; virtual  SelfDescribing() </span>;

\#endif

\[caption=\] \#ifndef OIWER\_NMVCHJKSD\_TYT\_48457\_GSDFUIE \#define
OIWER\_NMVCHJKSD\_TYT\_48457\_GSDFUIE

class Description;

class SelfDescribing <span> public: virtual void describeTo(Description&
description) const = 0; virtual  SelfDescribing() </span>;

\#endif

更重要的是，我们确信“抽象”和“信息隐藏”对于软件的重要性，这促使我将<span><span>public</span></span>接口总置于类的最前面成为我们的首选，<span><span>class</span></span>的特性正好与我们的期望背道而驰[^7]

不管你信仰那一个流派，切忌不能混合使用<span><span>class</span></span>和<span><span>struct</span></span>。在大量使用前导声明的情况下，一旦一个使用<span><span>struct</span></span>的类改为<span><span>class</span></span>，所有的前置声明都需要修改。

定义<span><span><span>C</span></span></span>风格的结构体时，摒弃<span><span>struct
tag</span></span>的命名风格。

<span><span>struct
tag</span></span>彻底抑制了结构体前置声明的可能性，从而阻碍了编译优化的空间。

反例：

\[caption=\] \#ifndef AQTYER\_023874\_NMHSFHKE\_7432378293 \#define
AQTYER\_023874\_NMHSFHKE\_7432378293

\#include &lt;cut/base/BaseTypes.h&gt;

typedef struct tag\_Cell <span> U16 cellId; U32 dlArfcn; </span>
T\_Cell;

\#endif

不给<span><span>struct</span></span>命名，而只给一个<span><span>typedef</span></span>的别名，也是极其不可取的（最糟糕的一种设计）。

反例：

\[caption=\] \#ifndef AQTYER\_023874\_NMHSFHKE\_7432378293 \#define
AQTYER\_023874\_NMHSFHKE\_7432378293

\#include &lt;cut/base/BaseTypes.h&gt;

typedef struct <span> U16 cellId; U16 dlArfcn; </span> T\_Cell;

\#endif

为了兼容<span><span><span>C</span></span></span>[^8]，并为结构体前置声明提供便利，如下解法是最合适的。

正例：

\[caption=\] \#ifndef AQTYER\_023874\_NMHSFHKE\_7432378293 \#define
AQTYER\_023874\_NMHSFHKE\_7432378293

\#include &lt;cut/base/BaseTypes.h&gt;

typedef struct T\_Cell <span> U16 cellId; U16 dlArfcn; </span> T\_Cell;

\#endif

如果性能不是关键问题，考虑使用<span><span>PIMPL</span></span>降低编译时依赖

反例：

\[caption=\] \#ifndef OIWTQNVHD\_10945\_HDFIUE\_23975\_HFGA \#define
OIWTQNVHD\_10945\_HDFIUE\_23975\_HFGA

\#include &lt;mockcpp/JmpOnlyApiHook.h&gt;

struct ApiHook

ApiHook(const void\* api, const void\* stub) : stubHook(api, stub)

private: JmpOnlyApiHook stubHook;

;

\#endif

正例：

\[caption=\] \#ifndef OIWTQNVHD\_10945\_HDFIUE\_23975\_HFGA \#define
OIWTQNVHD\_10945\_HDFIUE\_23975\_HFGA

struct ApiHookImpl;

struct ApiHook

ApiHook(const void\* api, const void\* stub);  ApiHook();

private: ApiHookImpl\* This;

;

\#endif

\[caption=\] \#include &lt;mockcpp/ApiHook.h&gt; \#include
&lt;mockcpp/JmpOnlyApiHook.h&gt;

struct ApiHookImpl

ApiHookImpl(const void\* api, const void\* stub) : stubHook(api, stub)
<span> </span>

JmpOnlyApiHook stubHook;

;

ApiHook::ApiHook( const void\* api, const void\* stub) : This(new
ApiHookImpl(api, stub)) <span> </span>

ApiHook:: ApiHook() <span> delete This; </span>

通过<span><span>ApiHookImpl\*
This</span></span>的桥接，在头文件中解除了对<span><span>JmpOnlyApiHook</span></span>的依赖，将其依赖控制在本编译单元内部。

template
--------

当选择模板实现时，请最大限度地降低编译时依赖。

当选择模板时，不得不将其实现定义在头文件中。当编译时依赖开销非常大时，编译模板将成为一种负担。设法降低编译时依赖，不仅仅为了缩短编译时间，更重要的是为了得到一个低耦合的实现。

反例：

\[caption=\] \#ifndef HGGAOO\_4611330\_NMSDFHW\_86794303\_HJHASI
\#define HGGAOO\_4611330\_NMSDFHW\_86794303\_HJHASI

\#include &lt;pub/typedef.h&gt; \#include &lt;pub/oss.h&gt; \#include
&lt;pub/commdef.h&gt; \#include &lt;oss/comm.h&gt; \#include
&lt;cut/base/Assertions.h&gt; \#include &lt;cut/base/Status.h&gt;

struct OssSender

OssSender(const PID& pid, const U8 commType) : pid(pid),
commType(commType) <span> </span>

template &lt;typename MSG&gt; Status send(const U16 eventId, const MSG&
msg) <span> CUB\_ASSERT\_TRUE(OSS\_SendAsynMsg(eventId, &msg,
sizeof(msg), commType,(PID\*)&pid) == OSS\_SUCCESS); return
CUB\_SUCCESS; </span>

private: PID pid; U8 commType;

;

\#endif

为了实现模板函数<span><span>send</span></span>，将<span><span>OSS</span></span>的一些实现细节暴露到了头文件中，包含<span><span>OssSender.h</span></span>的所有文件将无意识地产生了对<span><span>OSS</span></span>头文件的依赖。

提取一个私有的<span><span>send</span></span>函数，并将对<span><span>OSS</span></span>的依赖移入到<span><span>OssSender.cpp</span></span>中，对<span><span>PID</span></span>依赖通过前置声明解除，最终实现如代码所示。

正例：

\[caption=\] \#ifndef HGGAOO\_4611330\_NMSDFHW\_86794303\_HJHASI
\#define HGGAOO\_4611330\_NMSDFHW\_86794303\_HJHASI

\#include &lt;cut/base/Status.h&gt; \#include
&lt;cut/base/BaseTypes.h&gt;

struct PID;

struct OssSender

OssSender(const PID& pid, const U16 commType) : pid(pid),
commType(commType) <span> </span>

template &lt;typename MSG&gt; Status send(const U16 eventId, const MSG&
msg) <span> return send(eventId, (const void\*)&msg, sizeof(MSG));
</span>

private: Status send(const U16 eventId, const void\* msg, size\_t size);

private: const PID& pid; U8 commType;

;

\#endif

\[caption=\] \#include &lt;oss/OssSender&gt; \#include
&lt;pub/typedef.h&gt; \#include &lt;pub/oss.h&gt; \#include
&lt;pub/commdef.h&gt; \#include &lt;oss/comm.h&gt; \#include
&lt;cut/base/Assertions.h&gt;

Status OssSender::send(const U16 eventId, const void\* msg, size\_t
size) <span> CUB\_ASSERT\_TRUE(OSS\_SendAsynMsg(eventId, &msg,
sizeof(msg), commType,(PID\*)&pid) == OSS\_SUCCESS); return
CUB\_SUCCESS; </span>

识别哪些与泛型相关，哪些与泛型无关的知识，并解开此类编译时依赖是<span><span><span>C++</span></span></span>程序员的必备之技。此外，从这个例子看，仅仅为了使用<span><span>OSS\_SendAsynMsg</span></span>一个函数，缺包含了整个<span><span>oss</span></span>子系统，这是一种典型的物理设计的坏味道。

从另外一个角度看，<span><span>OssSender</span></span>的存在，其一让应用隔离了对平台的依赖，同时得到了物理依赖较小的设计。推而广之，良好的逻辑设计，往往能得到一个依赖最小的物理设计。

适时选择显式模板实例化<span><span>(Explicit Template
Instantiated)</span></span>，降低模板的编译时依赖。

模板的编译时依赖存在两个基本模型：包含模型，<span><span>export</span></span>模型。<span><span>export</span></span>模型受编译技术实现的挑战，最终被<span><span><span>C++</span></span></span><span><span>11</span></span>标准放弃。

此时，似乎我们只能选择包含模型。其实，存在一种特殊的场景，是能做到降低模板编译时依赖的。

反例：

\[caption=\] \#ifndef HGGQMVJK\_892302\_NGFSLEU\_796YJ\_GF5284 \#define
HGGQMVJK\_892302\_NGFSLEU\_796YJ\_GF5284

\#include &lt;quantity/Amount.h&gt;

template &lt;typename Unit&gt; struct Quantity

Quantity(const Amount amount, const Unit& unit) :
amountInBaseUnit(unit.toAmountInBaseUnit(amount))

bool operator==(const Quantity& rhs) const <span> return
amountInBaseUnit == rhs.amountInBaseUnit; </span>

bool operator!=(const Quantity& rhs) const <span> return !(\*this ==
rhs); </span>

private: const Amount amountInBaseUnit;

;

\#endif

\[caption=\] \#ifndef TYIW7364\_JG6389457\_BVGD7562\_VNW12\_JFH \#define
TYIW7364\_JG6389457\_BVGD7562\_VNW12\_JFH

\#include &lt;quantity/Quantity.h&gt; \#include
&lt;quantity/LengthUnit.h&gt;

typedef Quantity&lt;LengthUnit&gt; Length;

\#endif

\[caption=\] \#ifndef HG764MD\_NKGJKDSJLD\_RY64930\_NVHF977E \#define
HG764MD\_NKGJKDSJLD\_RY64930\_NVHF977E

\#include &lt;quantity/Quantity.h&gt; \#include
&lt;quantity/VolumeUnit.h&gt;

typedef Quantity&lt;VolumeUnit&gt; Volume;

\#endif

如上的设计，泛型类<span><span>Quantity</span></span>的实现都放在了头文件，不稳定的实现细节，例如计算<span><span>amountInBaseUnit</span></span>的算法变化等因素，将导致包含<span><span>Length</span></span>或<span><span>Volume</span></span>的所有源文件都需要重新编译。

更重要的是，因为<span><span>LengthUnit,
VolumeUnit</span></span>头文件的包含，如果因需求变化需要增加支持的单位，将间接导致了包含<span><span>Length</span></span>或<span><span>Volume</span></span>的所有源文件也需要重新编译。

如何控制和隔离<span><span>Quantity, LengthUnit,
VolumeUnit</span></span>变化的蔓延，而避免大部分的客户代码重新编译，从而与客户彻底解偶呢？可以通过显式模板实例化将模板实现从头文件中剥离出去，从而避免了不必要的依赖。

\[caption=\] \#ifndef HGGQMVJK\_892302\_NGFSLEU\_796YJ\_GF5284 \#define
HGGQMVJK\_892302\_NGFSLEU\_796YJ\_GF5284

\#include &lt;quantity/Amount.h&gt;

template &lt;typename Unit&gt; struct Quantity

Quantity(const Amount amount, const Unit& unit);

bool operator==(const Quantity& rhs) const; bool operator!=(const
Quantity& rhs) const;

private: const Amount amountInBaseUnit;

;

\#endif

\[caption=\] \#ifndef FKJHJT68302\_NVGKS97474\_YET122\_HEIW8565 \#define
FKJHJT68302\_NVGKS97474\_YET122\_HEIW8565

\#include &lt;quantity/Quantity.h&gt;

template &lt;typename Unit&gt; Quantity&lt;Unit&gt;::Quantity(const
Amount amount, const Unit& unit) :
amountInBaseUnit(unit.toAmountInBaseUnit(amount))

template &lt;typename Unit&gt; bool
Quantity&lt;Unit&gt;::operator==(const Quantity& rhs) const <span>
return amountInBaseUnit == rhs.amountInBaseUnit; </span>

template &lt;typename Unit&gt; bool
Quantity&lt;Unit&gt;::operator!=(const Quantity& rhs) const <span>
return !(\*this == rhs); </span>

\#endif

\[caption=\] \#ifndef TYIW7364\_JG6389457\_BVGD7562\_VNW12\_JFH \#define
TYIW7364\_JG6389457\_BVGD7562\_VNW12\_JFH

\#include &lt;quantity/Quantity.h&gt;

struct LengthUnit; struct Length : Quantity&lt;LengthUnit&gt; ;

\#endif

\[caption=\] \#include &lt;quantity/Quantity.tcc" \#include
&lt;quantity/LengthUnit.h&gt;

template struct Quantity&lt;LengthUnit&gt;;

\[caption=\] \#ifndef HG764MD\_NKGJKDSJLD\_RY64930\_NVHF977E \#define
HG764MD\_NKGJKDSJLD\_RY64930\_NVHF977E

\#include &lt;quantity/Quantity.h&gt;

struct VolumeUnit; struct Volume : Quantity&lt;VolumeUnit&gt; ;

\#endif

\[caption=\] \#include &lt;quantity/Quantity.tcc" \#include
&lt;quantity/VolumeUnit.h&gt;

template struct Quantity&lt;VolumeUnit&gt;;

<span><span>Length.h</span></span>仅仅对<span><span>Quantity.h</span></span>产生依赖;
特殊地，<span><span>Length.cpp</span></span>没有产生对<span><span>Length.h</span></span>的依赖，相反对<span><span>Quantity.tcc</span></span>产生了依赖。

另外，<span><span>Length.h</span></span>对<span><span>LengthUnit</span></span>的依赖关系也简化为声明依赖，而对其真正的编译时依赖，也控制在模板实例化的时刻，即在<span><span>Length.cpp</span></span>内部。

<span><span>LenghtUnit,
VolumeUnit的变化</span></span>，及其<span><span>Quantity.tcc</span></span>实现细节的变化，被完全地控制在<span><span>Length.cpp,
Volume.cpp</span></span>内部。

子类化优于<span><span>typedef</span></span>

如果使用<span><span>typedef</span></span>，如果存在对<span><span>Length</span></span>的依赖，即使是名字的声明依赖，除了包含头文件之外，别无选择。

另外，如果<span><span>Quantity</span></span>存在<span><span>virtual</span></span>函数时，<span><span>Length</span></span>还有进一步扩展<span><span>Quantity</span></span>的可能性，从而使设计提供了更大的灵活性。

反例：

\[caption=\] \#ifndef TYIW7364\_JG6389457\_BVGD7562\_VNW12\_JFH \#define
TYIW7364\_JG6389457\_BVGD7562\_VNW12\_JFH

\#include &lt;quantity/Quantity.h&gt;

struct LengthUnit; typedef Quantity&lt;LengthUnit&gt; Length;

\#endif

正例：

\[caption=\] \#ifndef TYIW7364\_JG6389457\_BVGD7562\_VNW12\_JFH \#define
TYIW7364\_JG6389457\_BVGD7562\_VNW12\_JFH

\#include &lt;quantity/Quantity.h&gt;

struct LengthUnit; struct Length : Quantity&lt;LengthUnit&gt; ;

\#endif

\[45mm\] <span><span>Controlling complexity is the essence of computer
programming.</span></span>

不可变性 {#ch:immutability}
========

我们无时无刻都在面临着新的变化，优秀的程序员擅于控制变化，尽量让对象变得不可变<span><span>(immutable)</span></span>，以便降低问题的复杂度。

const
-----

使用<span><span>const</span></span>替代<span><span>\#define</span></span>宏常量定义

使用<span><span>const</span></span>替代宏常量理由在经典的《<span><span>Effective
<span><span><span>C++</span></span></span></span></span>》著作中进行了详尽的描述，但往往受<span><span><span>C</span></span></span>语言根深蒂固的习惯常常被人遗忘。

当成员函数具有查询语义时应声明为<span><span>const</span></span>成员函数

此处具有查询语义的函数，泛指所有对对象状态未产生副作用的函数。<span><span>const</span></span>成员函数往往都以<span><span>get,
is, has, should</span></span>开头。

反例：

\[caption=<span>math/Rectangle.h</span>\] \#ifndef
EWRIUN9037\_NVHD6452\_JKLSDFUIE7562\_HGYE \#define
EWRIUN9037\_NVHD6452\_JKLSDFUIE7562\_HGYE

\#include “base/BaseTypes.h”

struct Rectangle

Rectangle(const U8 width, const U8 height);

U16 getArea(); U16 getPerimeter();

private: const U8 width; const U8 height;

;

\#endif

此例中未对那些具有查询语义的函数声明为<span><span>const</span></span>。<span><span>const</span></span>的存在不仅仅是为了提高编译时的安全性检查，更重要的是<span><span>const</span></span>建立了用户和类之间的契约关系，并传达了程序员良好设计的心声。

当对象以<span><span>pass-by-const-reference</span></span>传递时，用户只能调用其<span><span>const</span></span>成员函数；此外，<span><span>const</span></span>建立的契约，使<span><span>Replace
Temp with Query</span></span>成为可能。

正例：

\[caption=<span>math/Rectangle.h</span>\] \#ifndef
EWRIUN9037\_NVHD6452\_JKLSDFUIE7562\_HGYE \#define
EWRIUN9037\_NVHD6452\_JKLSDFUIE7562\_HGYE

\#include “base/BaseTypes.h”

struct Rectangle

Rectangle(const U8 width, const U8 height);

U16 getArea() const; U16 getPerimeter() const;

private: const U8 width; const U8 height;

;

\#endif

<span><span>const</span></span>成员函数不应该修改系统的状态

编译器只能保证<span><span>const</span></span>成员函数修改成员变量时提示错误，而未对修改全局变量，类的静态变量的情况进行检查，应杜绝此类情况的发生。

以<span><span>pass-by-reference-to-const</span></span>替代<span><span>pass-by-value</span></span>，以改善性能，并避免切割问题

虽然我们不提倡进行过早的优化，但也绝不提倡不成熟的劣化。<span><span>pass-by-reference-to-const</span></span>就是此句名言最好的一个例子。

当传递内置类型，迭代器及函数对象时，则可以<span><span>pass-by-value</span></span>。如果使用<span><span>const</span></span>修饰，往往可以改善<span><span>API</span></span>的可读性

其中，<span><span>Status, ActionId</span></span>分别是<span><span>U32,
U16</span></span>的<span><span>typedef</span></span>，但在设计<span><span>onDone</span></span>原型时，<span><span>const</span></span>的修饰不仅仅为了改善其安全性，更重要的是与<span><span>TransactionInfo</span></span>的<span><span>reference-to-const</span></span>形成对称性[^9]，改善了<span><span>API</span></span>的美感。

反例：

\[caption=<span>trans-dsl/listener/TransactionListener.h</span>\]
\#ifndef UTJKLFJS\_467867\_NBHD83562\_HETRIO\_75649 \#define
UTJKLFJS\_467867\_NBHD83562\_HETRIO\_75649

\#include “base/Status.h” \#include “trans-dsl/concept/ActionId.h”

struct TransactionInfo;

struct TransactionListener <span> virtual Status onDone(const
TransactionInfo&, const ActionId&, const Status&) </span>;

\#endif

正例：

\[caption=<span>trans-dsl/listener/TransactionListener.h</span>\]
\#ifndef UTJKLFJS\_467867\_NBHD83562\_HETRIO\_75649 \#define
UTJKLFJS\_467867\_NBHD83562\_HETRIO\_75649

\#include “base/Status.h” \#include “trans-dsl/concept/ActionId.h”

struct TransactionInfo;

struct TransactionListener <span> virtual Status onDone(const
TransactionInfo&, const ActionId, const Status) </span>;

\#endif

当返回的是一个新对象时，必须返回其值类型;
更有甚者，返回<span><span>const</span></span>的值类型将改善编译时的安全性

反例：

\[caption=<span>math/Rectangle.h</span>\] \#ifndef
EWRIUN9037\_NVHD6452\_JKLSDFUIE7562\_HGYE \#define
EWRIUN9037\_NVHD6452\_JKLSDFUIE7562\_HGYE

\#include “base/BaseTypes.h”

struct Rectangle

Rectangle(const U8 width, const U8 height);

U16 getArea() const; U16 getPerimeter() const;

bool operator==(const Rectangle& rhs) const; bool operator!=(const
Rectangle& rhs) const;

Rectangle& operator+=(const Rectangle& rhs) const; Rectangle&
operator+(const Rectangle& rhs) const;

private: const U8 width; const U8 height;

;

\#endif

<span><span>operator+</span></span>返回的是一个新实例，返回值必须设计为值类型。如果提供<span><span>const</span></span>的修饰能够加强编译时的安全性检查。此外，需要注意的是<span><span>operator+=</span></span>返回的是修改后的`*this`对象引用。

正例：

\[caption=<span>math/Rectangle.h</span>\] \#ifndef
EWRIUN9037\_NVHD6452\_JKLSDFUIE7562\_HGYE \#define
EWRIUN9037\_NVHD6452\_JKLSDFUIE7562\_HGYE

\#include “base/BaseTypes.h”

struct Rectangle

Rectangle(const U8 width, const U8 height);

U16 getArea() const; U16 getPerimeter() const;

bool operator==(const Rectangle& rhs) const; bool operator!=(const
Rectangle& rhs) const;

Rectangle& operator+=(const Rectangle& rhs) const; const Rectangle
operator-(const Rectangle& rhs) const;

private: const U8 width; const U8 height;

;

\#endif

不能返回局部对象的引用或指针。

返回值类型还是引用类型常常会困扰部分<span><span><span>C++</span></span></span>程序员。其实规则非常简单，返回值对象当且仅当需要创建新对象的时候，此时如果企图返回引用或指针，将导致运行时异常。

不可变类
--------

鼓励设计不可变类<span><span>(Immutable
Class)</span></span>表达值对象<span><span>(Value
Object)</span></span>的语义

不可变类的每一个实例在创建的时候就包含了所有必要的信息，其对象在整个生命周期中都不会发生变化。不可变类具有如下几方面的优势：

<span>*<span>相对于可变对象的复杂的状态空间，不可变类仅有一个状态，容易设计、实现和控制</span>*</span>

<span>*<span>不可变类本质上是线程安全的，它们不需要同步</span>*</span>

<span>*<span>不可变类可被自由地共享，重用对象是一种良好设计的习惯</span>*</span>

设计不可变类，需遵循如下规则：

<span>*<span>不能提供修改对象状态的方法</span>*</span>

<span>*<span>保证类不能被扩展，切忌提供<span><span>virtual
destructor</span></span></span>*</span>

<span>*<span>所有成员变量和方法都是<span><span>const</span></span></span>*</span>

<span>*<span>所有成员变量都是<span><span>private</span></span></span>*</span>

<span>*<span>绝不允许重新赋值，但允许复制出新的实例</span>*</span>

不可变类唯一的缺点就是，对于每一个不同的值都需要一个单独的对象。当需要创建大量此类对象时，性能可能成为瓶颈。当性能成为关键瓶颈的时候，为不可变类设计可变配套类是一种典型的设计方式。

例如<span><span>Java</span></span>的<span><span>JDK</span></span>中，<span><span>String</span></span>被设计为不可变类，但在诸如字符串需要大量的替换、追加等场景下，性能可能成为关键瓶颈；<span><span>JDK</span></span>提供了<span><span>StringBuilder</span></span>的可变配套类来解决此类问题。

上例讲解的<span><span>Rectangle</span></span>类也是一种典型的不可变类的设计。

尽量使类的可变性最小化

坚决抵制为每一个<span><span>get</span></span>函数都写一个<span><span>set</span></span>函数，除非存在一个很好的理由。构造函数的职责就是来完成对象的初始化，并建立起所有的约束关系。除非有很好的理由，不要在构造函数之外提供其他公开的初始化方法。

\[45mm\] <span><span>Write programs for people first, computers
second.</span></span>

命名 {#ch:naming}
====

良好的命名将改善代码的表现力，与其说命名是一门技术，不如说它是一门艺术。必须坚持、并慎重地给程序中的每一个实体取好名字，让其名副其实，代码的可读性将得到极大的改善。

Baby Names
----------

遵守统一的命名规范

一些程序设计语言，从诞生的时刻就有着自己的文化背景，整个社区有着统一的命名规则。但<span><span><span>C++</span></span></span>在社区中存在众多的命名风格，有的与时俱进，也非常人性化；有的则已经与现代软件工程格格不入[^10]。

下文罗列了一些<span><span><span>C++</span></span></span>典型的命名规范供参考。每一种命名规范都有自身自己的优缺点，团队应该根据自身的实际情况选择适合自己的命名规范。最重要的是，团队应遵循统一的命名规范，不应该出现两种或两种以上的命名风格。

我们推荐团队使用下文中任意一种命名风格，但如果由于历史遗留原因导致革新非常困难，而无法采用新的命名规范，团队依然要保持统一的命名规范，避免出现多种命名风格。

还有一种命名风格与上一种风格类同，只是成员函数/函数都以大写开头的驼峰命名。

第三种命名风格，主要体现在标准库或<span><span>Boost</span></span>准标准库社区，其规则非常简单，下划线分割的全小写，或下划线分割的全大写。

绝不使用汉语拼音命名

必须实用标准的英语命名程序实体，不允许实用汉语拼音。

类名应该是名词或名词短语；接口可以是形容词; 方法名应该是动词或动词短语

接口可以是形容词，最为常见的就是定义能力接口，即以<span><span>-able</span></span>结尾。

反例：

\[caption=<span>thread/Runnable.h</span>\] \#ifndef
LJKYIUERUIQ09857983\_NVHKJKHA86100494\_JGYQPIPWNC \#define
LJKYIUERUIQ09857983\_NVHKJKHA86100494\_JGYQPIPWNC

\#include “base/Keywords.h”

// 接口必须是形容词或名词，不允许是动词 DEFINE\_ROLE(Run) <span>
ABSTRACT(void run()); </span>;

\#endif

正例：

\[caption=<span>thread/Runnable.h</span>\] \#ifndef
LJKYIUERUIQ09857983\_NVHKJKHA86100494\_JGYQPIPWNC \#define
LJKYIUERUIQ09857983\_NVHKJKHA86100494\_JGYQPIPWNC

\#include “base/Keywords.h”

DEFINE\_ROLE(Runnable) <span> ABSTRACT(void run()); </span>;

\#endif

如果函数返回值为<span><span>bool</span></span>，加上<span><span>is, has,
can, should, need</span></span>将会增强语意

反例：

bool readPassword = true;

至少存在两种解释，

<span>*<span><span><span>We need to read the
password</span></span></span>*</span>

<span>*<span><span><span>The password has already been
read</span></span></span>*</span>

正例：

bool needPassword = true; bool userIsAuthenticated = true;

丰富你的单词库，在面对具体问题时你具有更多的<span><span>Colorfull
Words</span></span>

如<span><span>*<span>表</span><span><span>\[tbl:colorful-words\]（第页）</span></span>*</span></span>所示，同一概念是有很多种表达方式的。

名字在明确意图的前提下越短越好

反例：

ControllerForEfficientHandlingOfStrings
ControllerForEfficientStorageOfStrings

因为这两个类名实在是太相似了，一时间很难区分。当别人打算复用你的代码时，必然承受着巨大的记忆包袱。

另外，实体名称的长度应该于作用域的大小成正比。如果是一个实体暴露在全局命名空间，则需要适当增加名字长度，防止名字冲突[^11]。相反地，在一个很小的函数之内可见的局部变量，尤其在一个短小的<span><span>for</span></span>循环作用域内，完全没有必要取一个很长的名字。

反例：

\[caption=“trans-dsl/listener/MutilEventListener.cpp”\] void
MutilEventListener::onEventDone() <span> for(int index=0;
index!=listeners.size(); index++) <span>
listeners\[index\].onEventDone(); </span> </span>

优秀的程序员在命名的长短的取舍总是游刃有余，但从来没有降低过代码的意图。

正例：

\[caption=“trans-dsl/listener/MutilEventListener.cpp”\] void
MutilEventListener::onEventDown() <span> for(int i=0;
i!=listeners.size(); i++) <span> listeners\[i\].onEventDone(); </span>
</span>

程序中每个实体都应该有一个意图明确<span><span>(Intention-Revealing)</span></span>的名称

反例：

vector&lt;vector&lt;int&gt; &gt; getThem()

vector&lt;vector&lt;int&gt; &gt; list1;

for(auto x : theList) <span> if(x\[0\] == 4) <span> list1.add(x);
</span> </span>

return list1;

<span>*<span><span><span>vector&lt;vector&lt;int&gt;
&gt;</span></span>的语法令人抓狂</span>*</span>

<span>*<span><span><span>getThem</span></span>让人看不清楚它的本意</span>*</span>

<span>*<span><span><span>theList</span></span>到底是什么东西？</span>*</span>

<span>*<span><span><span>0</span></span>下标意味着什么？<span><span>4</span></span>又意味着什么？</span>*</span>

<span>*<span><span><span>list1</span></span>就是为了编译通过吗？</span>*</span>

换一个好名字之后，并对数据结构进行了简单的封装。

正例：

\#include &lt;vector&gt;

struct Cell

bool isFlagged() const;

private: std::vector&lt;int&gt; states;

;

using Cells = std::vector&lt;Cell&gt;;

重构之后的效果，抽象和可读性得到了改善[^12]。

Cells getFlaggedCells() const

Cells flaggedCells;

for(auto &cell : gameBoard) <span> if(cell-&gt;isFlagged()) <span>
flaggedCells.push\_back(\*cell); </span> </span>

return flaggedCells;

避免在名称中携带数据结构的信息

别用<span><span>accountList，accountArray</span></span>指定一组账号，当包含<span><span>Account</span></span>的容器不在是一个<span><span>List</span></span>或<span><span>Array</span></span>的时候，就会引发错误的判断。所以，用<span><span>accountGroup</span></span>，<span><span>bunchOfAccounts</span></span>，甚至直接使用<span><span>accounts</span></span>，情况都会更好一些。

<span><span>Noise Words are
Redundant</span></span>，消除噪声后将得到一个更加精准的名字

如<span><span>*<span>表</span><span><span>\[tbl:redundant-words\]（第页）</span></span>*</span></span>所示，消除冗余的噪声，将得到一个更加直观、更漂亮的名字。

使用<span><span>Domain</span></span>领域内的名称，将更直白地表明你的设计，增强领域内成员的沟通

<span>*<span><span><span>Factory, Visitor,
Repository</span></span></span>*</span>

<span>*<span><span><span>valueOf, of, getInstance, newInstance,
newType</span></span></span>*</span>

<span>*<span><span><span>AppendAble, Closeable, Runnable, Readable,
Invokable</span></span></span>*</span>

当使用<span><span>Visitor</span></span>，你在使用访问者模式；当使用<span><span>valueOf,
of</span></span>，你在使用静态工厂方法。领域内的命名风格，让领域内的成员更加快捷地理解你的设计意图。

匈牙利命名
----------

摒弃匈牙利命名

匈牙利命名曾风靡一时。但是，现代编程语言具有更丰富的类型系统；人们更趋于使用更小的类，更短的函数，让每一个变量定义都在可控的视野范围之内；此外，<span><span>IDE</span></span>变得越来智能和强大，匈牙利命名反而变成了一种噪声和肉刺。

摒弃给成员变量加前缀，或后缀

为类的成员变量增加<span><span>m\_</span></span>前缀同样没有必要。与其在在犹豫加前缀还是不加前缀，不如花费更多的时间将类分解；当类足够小，职责足够单一，使用现代<span><span>IDE</span></span>的着色功能，成员变量和普通变量一眼便能识别开来[^13]。

摒弃常量的前缀

常量前增加<span><span>k\_</span></span>前缀同样没有必要，如果熟悉了大写、下划线隔开的命名风格，<span><span>k\_</span></span>前缀完全属于多余。

摒弃接口和类的前缀

在接口前增加<span><span>I\_</span></span>，在类前增加<span><span>C\_</span></span>，同样完全没有必要，它只能对重构带来阻力，百害而无一利。

反例：

\[caption=<span>trans-dsl/sched/IAction.h</span>\] \#ifndef
NVCHKJSD903085\_JGOIUUE906894\_VBKSJKJA075774 \#define
NVCHKJSD903085\_JGOIUUE906894\_VBKSJKJA075774

\#include “base/Keywords.h” \#include “base/Status.h”

struct TransactionInfo;

DEFINE\_ROLE(IAction) <span> ABSTRACT(Status exec(const
TransactionInfo&)); </span>;

\#endif

<span><span>Action</span></span>前面的<span><span>I</span></span>就是一句废话。如果非得在接口与实现中选择，宁愿选择实现中增加<span><span>Impl</span></span>后缀。

注释
----

注释不如花费更多时间给实体取一个好名字，让其名副其实

反例：

int time; // elapsed time in days

正例：

int elapsedTimeInDays;

注释应成为一种羞耻的活动，当需要添加注释的时候，往往是改善设计的最好时机。

消除所有没有必要的注释

没有携带任何信息量的注释都是没有必要的。如下列的注释，维护它简直就是一种巨大的包袱，有时候它的存在就像一个笑话。它就像在挑战读者的智商，谁都知道它是一个构造函数。

反例：

/\*\* \* Constructor \*/ InvokedAtMost(const unsigned int times);

/\*\* \* @param Invocation \* @return bool \*/ bool matches(const
Invocation& inv) const;

消除所有误导性、过时的、与设计实现不匹配的注释

如果注释和代码已经失去匹配，意图甚至是相反的。这样的注释如果继续存在，贻害的肯定不止一个人。“假如代码和注释不一致，那么很可能两者都是错误的”，<span><span>Norm
Schryer</span></span>形象地描述了不一致的注释给代码维护者带来的困扰。

消除所有日志型、归属、签名的注释

修正一个<span><span>bug</span></span>时，都需要在函数头的注释表中记录被次修改的内容。放弃这种“好”习惯吧，请将这些详细的信息提交给源代码控制系统，那里是此类注释最好的归所。

消除所有<span><span>//end if, //end while, //end for, // end
try</span></span>的注释

因为逻辑太过于冗长、复杂，又为了增强可读性，往往在花括号后面标记<span><span>//end
if, //end while, //end for, // end
try</span></span>，这往往是简化表达式、提取函数的最佳时机。

已经被注释掉的代码，应该立即删除

不要珍惜这些冗余的代码，害怕丢掉这些代码而买不到后悔药。你要相信，从源代码控制系统中追回这份被删除的代码易如反掌。

在需要注释的时候，一定要加注释

因公司版权的保护，需要增加版权法律信息注释[^14]。幸运的是，这类问题可以通过代码模板轻松解决，不会成为造成程序员的任何负担。

在已经尽全力也无法用代码表述清楚时，增加必要的注释会使代码更加容易被别人理解和维护。在这些场景下，注释将成为我们最后一根救命稻草。

<span>*<span>代码无法明确的意图也需要增加注释</span>*</span>

<span>*<span>如果在代码中存在特殊的陷阱、实现手法等情况，此时注释变得尤为宝贵</span>*</span>

例如，当操作复杂的位运算时，提供比特位的内存映像的注解，将有利于加快读者阅读代码的速度。

正例：

// Fast version of “hash = (65599 \* hash) + c” hash = (hash &lt;&lt; 6)
+ (hash &lt;&lt; 16) - hash + c;

当定义难以理解的正则表达式时，提供更直观的格式说明，同样可以改善对代码的理解。

正例：

// kk::mm::ss, MM dd, yyyy std::string timePattern = “\
d<span>2</span>:\
d<span>2</span>:\
d<span>2</span>,\
d<span>2</span>\
d<span>2</span>,\
d<span>4</span>”;

\[45mm\] <span><span>Do the simplest thing that could possibly
work.</span></span>

简化逻辑 {#ch:simple-logic}
========

简化控制逻辑
------------

<span><span>YODA Notation</span></span>已经是过去时

if (length &lt;= MAX\_STREAM\_LEN)

要比

if (MAX\_STREAM\_LEN &gt;= length)

更具有表达力。再看一个例子，

while (bytesReceived &lt; bytesExpected)

要比

while (bytesExpected &gt; bytesReceived)

更具由表达力。因为前者更加符合人类的思维，或这说更符合英语的表达习惯，<span><span>“if
you are at least 18 years old.”</span></span>明显比<span><span>“if 18
years is less than or equal to your
age”</span></span>更加符合英语表达习惯。是的，英语更加习惯将稳定的一侧放在右边<span><span>(right-hand
side)</span></span>。

但是，在<span><span><span>C</span></span></span>或者<span><span><span>C++</span></span></span>语言中，如果<span><span>==</span></span>被误用为<span><span>=</span></span>，则可能发生副作用的危险，而且编译时并不能做到安全的检查，从而产生了严重的<span><span>bug</span></span>。

// 缺少等号，造成严重的运行时错误 if (ptr = NULL)

幸运的是，现代编译器对此类误用通常报告警告信息；如果保持<span><span>TDD</span></span>开发节奏，小步前进，此类低级错误很难逃出测试的法网。

正例：

if (ptr == NULL)

反例：

if (NULL == ptr)

在简单逻辑的情况下，鼓励使用<span><span>?:</span></span>三元表达式；但是，当表达式变得非常复杂时，<span><span>if-else</span></span>可能是更好的选择

反例：

if (hour &gt;= 12) <span> time += “pm”; </span> else <span> time +=
“am”; </span>

正例：

time\_str += (hour &gt;= 12) ? “pm” : “am”;

但很多程序员往往因为习惯了`if-else`而忽视了这种简洁的表达式。但是，当表达式变得非常复杂时，`if-else`可能是更好的选择。

反例：

return exponent &gt;= 0 ? mantissa \* (1 &lt;&lt; exponent) : mantissa /
(1 &lt;&lt; -exponent);

正例：

if (exponent &gt;= 0) <span> return mantissa \* (1 &lt;&lt; exponent);
</span> else <span> return mantissa / (1 &lt;&lt; -exponent); </span>

当逻辑表达式已经具有<span><span>true或false</span></span>语义时，则无需显示地加上<span><span>true或false</span></span>

反例：

bool exist = nodes.contains(NodeId(2)) ? true : false; if(exist == true)
<span> ... </span>

正例：

if(nodes.contains(NodeId(2)) <span> ... </span>

避免函数嵌套过深，擅用卫语句从函数中提前返回，或从嵌套的语句中提前返回；但绝对不滥用<span><span>break,
continue</span></span>

嵌套过深的函数，将迫使读者跟踪运行时<span><span>stack</span></span>，同样给读者增加过重的记忆包袱。

反例：

if (userResult == SUCCESS) <span> if (permissionResult != SUCCESS)
<span> reply.writeError(permissionResult); return; </span>
reply.writeError(“”); </span> else <span> reply.writeError(usrResult);
</span>

正例：

if (userResult != SUCCESS) <span> reply.writeError(usrResult); return;
</span>

if (permissionResult != SUCCESS) <span>
reply.writeError(permissionResult); return; </span>

reply.writeError(“”);

虽然在代码阅读过程中<span><span>break, continue,
return</span></span>常常打断了人的思维。但在函数短小，意图明确的情况下，<span><span>break,
continue,
return</span></span>相反能给人一种“跳过此项”的特殊意图，代码嵌套逻辑得到了改善。

擅用解释型变量，或提供意图明确的、内联的提取函数

解释型变量，或提取函数的重构手法有利于改善代码的可读性，往往后者更具有表达力。

反例：

if (line.split(“:”)\[0\].trim() == “root”)

正例：

String userName = line.split(“:”)\[0\].trim(); if (userName == “root”)
<span> ... </span>

<span><span>split</span></span>函数将字符串按照指定的正则表达式进行拆分，并提供一个良好的意图变量，将大大改善逻辑的清晰度。

将局部变量的作用域最小化

这条规则可能对从<span><span><span>C</span></span></span>转变过来的<span><span><span>C++</span></span></span>程序员更有指导意义，但改变这样的陋习可能需要一些适应的时间。例如局部于<span><span>for</span></span>的循环变量，当它的使命完成之后，应立即销毁它，避免这个变量被再次使用的风险。

map&lt;string, string&gt; addressBook; for (auto &entry : addressBook)
<span> std::cout &lt;&lt; entry-&gt;first &lt;&lt; “,” &lt;&lt;
entry-&gt;second &lt;&lt; std::endl; </span>

\[45mm\] <span><span>Premature optimization is the root of all
evil.</span></span>

<span><span>On the other hand, we cannot ignore
efficiency.</span></span>

函数设计 {#ch:functions-operators}
========

函数
----

避免过长，嵌套过深的函数实现

我讨厌长函数，犹如讨厌重复一样。长函数往往伴随着复杂的逻辑判断，过深嵌套逻辑。

但也必要硬性地规定团队函数不能超过固定的行，因为这个规则很容易被打破。如果大家都遵循良好的设计原则，养成良好的职责分离的设计的基本素养，实现出来的函数大多平均都在<span><span>5</span></span>行以内，或者更少。这绝对不是理想，已经存在众多的、典型的成功案例。

只做一件事，并做好这件事

这是<span><span>SRP</span></span>在函数实现中的一个具体体现。一个函数只应该承担一个唯一的职责，如果函数名伴随<span><span>and</span></span>，或将查询和命令混合往往是违背此原则的信号。

一般地，如果函数只是做了该函数名称下同一抽象层次上的几个小步骤，则函数还是只做了一件事情。函数就是将一个大一点的概念拆分成级别稍微低一点、并在同一个抽象层次的一系列步骤的过程。

函数中的每一个语句都在一个相同的抽象层次上

如果函数中混杂不同抽象层次的代码，往往让人感到迷惑，理解代码的逻辑，需要读者陷入到细节之中而不能自拨。

<span><span>Kent Beck</span></span>建议使用<span><span>Compose
Method</span></span>分解长函数；<span><span>Martin
Flower</span></span>也建议使用<span><span>Extract
Method</span></span>进行函数提取。<span><span>Extract
Method</span></span>最重要的就是识别出代码中的抽象层次，并梳理出主干，按照自顶向下的规则实现函数的。

函数提取常常要遵守如下3个基本原则：

<span>*<span><span><span>在同一个抽象层次</span></span></span>*</span>

<span>*<span><span><span>给一个直观的，意图明确的好名字</span></span></span>*</span>

<span>*<span><span><span>实现对称性</span></span></span>*</span>

正如<span><span>Bob</span></span>大叔提到的那样:
程序就像是一系列的以<span><span>TO</span></span>起头的段落，每一段落都描述了当前抽象层次的逻辑，并引用下一抽象层次的，以<span><span>TO</span></span>开头的段落。

下例虽然以<span><span>Java</span></span>为例，但重点没有偏离，规则同样适用于<span><span><span>C</span></span></span>/<span><span><span>C++</span></span></span>。

\[caption=<span>java.util.List</span>\] public class List&lt;E&gt;
<span> public void add(E element) <span> if (!readOnly) <span> int
newSize = size + 1; if (newSize &gt; elements.length) <span> Object\[\]
newElements = new Object\[elements.length + 10\]; for (int i = 0; i &lt;
size; i++) newElements\[i\] = elements\[i\]; elements = newElements;
</span> elements\[size++\] = element; </span> </span> </span>

提取函数之后，使算法的骨骼显而易见。

\[caption=<span>java.util.List</span>\] public class List&lt;E&gt;

public void add(E element)

if (readOnly) return;

if (atCapacity()) grow();

addElement(element);

提取函数往往受到性能偏执狂的抨击，他们认为过多的函数提取将成为性能的主要瓶颈。<span><span>2-8</span></span>原则将彻底击垮所有不靠谱的言论，与其纠结于函数调用的开销，不如花费更多的时间去优化和改善那些至关重要的算法和关键代码。

检查参数的有效性

绝大部分的函数对于传递的参数都有限制，这时需要在函数执行之前完成参数的合法性校验。<span><span><span>C</span></span></span>/<span><span><span>C++</span></span></span>虽不能天然地支持“按契约设计”，但前置的参数检查将大大改善程序的健壮性。

分离查询与指令

函数应该只拥有清晰明确的、唯一的职责。如果函数既修改对象状态，又返回对象的状态信息，则常常会导致混乱。产生副作用的指令操作，都是系统状态的一种变更，将产生时序上的耦合和顺序的依赖。尤其当查询和指令混合在一起的时候，查询函数的无副作用的优点将不复存在；如果一个函数名本身具有查询语义，但混合了指令操作，将产生更大的反直觉。

使用<span><span>Null Object</span></span>替代空指针

校验空指针是一件及其繁琐的事情，优秀的程序员通过各种技巧绕开这些冗余的操作。例如参数通过引用传递，另外一种常见的手段就是<span><span>Null
Object</span></span>[^15]。

对于参数类型，返回值类型，优先使用接口类型

遵循按接口编程的良好习惯，是优秀设计师的基本素养。

对于<span><span>bool</span></span>参数，优先使用两个元素的枚举类型

反例：

Thermometer::newInstance(true);

正例：

Thermometer::newInstance(CELSIUS);

可以通过内部的<span><span>private</span></span>函数来解决代码复用的问题。也就是说，带<span><span>bool</span></span>参数的函数依然存在，只不过被<span><span>private</span></span>，以便实现对枚举参数的函数的代码复用。

永远不要导出具有相同参数数目的的重载方法

重载是一种编译时的多态。只要函数具有相同名字，但参数数目，类型不同，即为重载。但滥用往往会误导使用<span><span>API</span></span>的程序员，尤其在具有相同参数数目的重载方法时，程序员需要清晰地知道所有类型的隐式转换规则，即其重载匹配规则，这无疑是一种没必要的负担。

\[caption=<span>io/ObjectOutputStream.h</span>\] \#ifndef
JAAA\_1295\_BBVBAA\_GFYQQPPAAMZZ0092444\_NDFQQAA \#define
JAAA\_1295\_BBVBAA\_GFYQQPPAAMZZ0092444\_NDFQQAA

struct ObjectOutputStream <span> void write(bool); void write(char);
void write(short); void write(int); void write(long); void write(float);
void write(double); </span>;

\#endif

面对疑难的时候，抛弃重载往往能得到更不容易犯错的解决方案。

\[caption=<span>io/ObjectOutputStream.h</span>\] \#ifndef
JAAA\_1295\_BBVBAA\_GFYQQPPAAMZZ0092444\_NDFQQAA \#define
JAAA\_1295\_BBVBAA\_GFYQQPPAAMZZ0092444\_NDFQQAA

struct ObjectOutputStream <span> void writeBool(bool); void
writeChar(char); void writeShort(short); void writeInt(int); void
writeLong(long); void writeFloat(float); void writeDouble(double);
</span>;

\#endif

使用<span><span>explicit</span></span>显式地禁止类型的隐式转换

隐式类型转换往往无声无息地被执行，通过<span><span>explicit</span></span>便能通过编译器清晰地捕获的所有隐式转换的事件，以便供程序员进一步决策。

避免实现火车失事的代码

反例：

String outputDir = ctxt.getOptions().getScratchDir().getAbsolutePath();

本例虽然使用<span><span>Java</span></span>语言编写，但这不影响对火车失事问题的理解。如果其调用链如果某一环节出现了问题，则整个调用将出现失败。这类串联的调用违反了<span><span>Demeter</span></span>法则，<span><span>ctxt</span></span>对象包含了多个选项，每个选项中存在一个临时目录，每个目录都有一个绝对路径，所有的知识都毫无保留地暴露给了用户。

仔细分析一下代码，再看看其中一个模块是如何使用这个<span><span>outputDir</span></span>的。

String outFile = outputDir + File.SEPERATOR + className + “.class”;
BufferedOutputStream bos = new BufferedOutputStream(new
FileOutputStream(outFile));

所有的一切都是为了创建指定名称的临时文件，理想的实现应该将所有本应该隐藏的知识归并到<span><span>ctxt</span></span>中实现。

正例：

BufferedOutputStream bos = ctxt.createScratchFileStream(className);

重载操作符
----------

重载运算符必须保持原有操作符的语义

如果重载运算符改变了程序员对固有知识的理解，将加大放错的几率。

谨慎地使用转换运算符

转换运算符因为其隐式转换而变得非常神秘，需谨慎使用。并非在任何场景都不使用转换操作符，在合适的情况下使用装换运算符，能够得到更为简洁的代码。

优先使用前置<span><span>++operator</span></span>

当重载了<span><span>++operator</span></span>的类对象，例如迭代器，更提倡使用<span><span>++operator</span></span>，这是提升效率的一种举措。

使用<span><span>operator\*,
operator-&gt;</span></span>实现类的包装或修饰

<span><span>operator\*,
operator-&gt;</span></span>操作符是提供包装和修饰功能的特殊工具，是一种典型的间接技术[^16]。它的最大优势是为用户提供良好的、人性化间接操作接口。

<span><span>std::unique\_ptr,
std::shared\_ptr</span></span>等智能指针，最关键的也是重载了这两个操作符，从而实现了操作智能指针犹如操作原始指针一般。

<span><span>Placment</span></span>本身也是一个包装器，只不过它修饰的是一块原始的内存。通过<span><span>operator\*,
operator-&gt;</span></span>可方便地操作寄存在原始内存上的<span><span>T</span></span>对象。

<span><span>AutoMsg</span></span>也是一个较为经典的例子，<span><span>AutoMsg</span></span>将消息对象的构造搬迁到了堆上进行初始化，从而避免了由于消息过大而导致的栈溢出的风险。当函数调用出栈时，内存自动释放。

\[caption=<span>base/AutoMsg.h</span>\] \#ifndef
AA\_TTYSFLNVHSL\_375BBGGH7754420010MHHSLJEROLJKD \#define
AA\_TTYSFLNVHSL\_375BBGGH7754420010MHHSLJEROLJKD

template &lt;typename Msg&gt; struct AutoMsg

AutoMsg() : msg(new Msg)

 AutoMsg() <span> delete msg; </span>

Msg& operator\*() <span> return \*msg; </span>

Msg\* operator-&gt;() <span> return msg; </span>

private: Msg\* msg;

;

\#endif

\[caption=<span>money/RemoteAccount.h</span>\] \#ifndef
QLALK\_YRUUUTIIT00475\_NVBBAKKF\_6455BCHKAK\_YQQAMGH \#define
QLALK\_YRUUUTIIT00475\_NVBBAKKF\_6455BCHKAK\_YQQAMGH

\#include &lt;money/domain/Account.h&gt; \#include
&lt;money/msg/TransMoneyMsg.h&gt; \#include &lt;base/Asserter.h&gt;

struct RemoteAccount

Status transMoneyTo(const Account& to)

AutoMsg&lt;TransMoneyMsg&gt; msg;

ASSERT\_SUCC\_CALL(buildMsg(\*msg)); ASSERT\_SUCC\_CALL(sendMsg(to,
\*msg));

return SUCCESS;

private: Status buildMsg(TransMoneyMsg&) <span> // no implement </span>

Status sendMsg(const Account& to, const TransMoneyMsg& msg) <span> // no
implement </span>

;

\#endif

\[45mm\] <span><span>There are two ways of constructing a software
design. One way is to make it so simple that there are obviously no
deficiencies. And the other way is to make it so complicated that there
are no obvious deficiencies.</span></span>

整洁测试 {#ch:clean-test}
========

TDD
---

<span><span>TDD</span></span>遵循三定律

<span>*<span>在编写不能通过的测试前，不可编写生产代码</span>*</span>

<span>*<span>只可编写刚好无法通过的测试，不能编译也算不通过</span>*</span>

<span>*<span>只可编写刚好足以通过当前失败测试的生产代码</span>*</span>

关于测试驱动请参考<span><span>Kent Beck的著作《Test-Driven Development,
by example》</span></span>。

测试名称遵循<span><span>Given-When-Then</span></span>

这是流行的<span><span>BDD，行为驱动测试</span></span>命名规范，当阅读测试用例时，或当测试失败时，这样的命名风格非常有利于行为的描述。

摒弃原始的<span><span>TestXXX</span></span>的风格吧，因为它不能清晰表达<span><span>TDD</span></span>的意图。

每一个测试一个概念

这是<span><span>SRP</span></span>在测试用例中的体现，当测试用例失败的时候，能够清晰地知道测试失败的原因。

一个概念往往只会有一个断言来描述，出现数目众多的断言往往违背了此规则。

将具有相同测试环境的用例放在同一个测试套件中

将构造测试环境及清理测试环境的代码分别放在<span><span>Setup</span></span>及<span><span>Teardown</span></span>中，可以消除重复的代码，实现代码的最大可复用性。

测试应该像文档一样清晰

测试用例是理解系统行为的最佳途径，也是最实时、最权威的文档。

测试更应该是像一个例子

测试不仅仅为了测试而测试，更重要的是对系统行为的描述。

测试用例中不应该存在复杂的循环、条件控制语句

测试用例对可读性的要求非常高，如果出现大量的循环、条件控制语句，将大大地损害了用例的可读性。一般地，测试用例应该是有若干条陈述句所组成，越简单越好。

设计面向特定领域的测试语言是值得的

根据领域问题，设计特定领域描述语言<span><span>DSL</span></span>，将改善用例的可读性和维护性。

[^1]: <span><span>Agile Software Development, Principles, Patterns, and
    Practices, Robert C. Martin</span></span>

[^2]: <span><span>TAB</span></span>一般配置为2或4个空格，所有的编辑器都提供了类似的配置接口。

[^3]: 例如<span><span>Eclipse</span></span>可以配置头文件的代码模板，其他<span><span>IDE</span></span>也存在类似的功能。

[^4]: 其实是弱编译时依赖，但为了避免代码重复，所以一般选择直接包含<span><span>typedef</span></span>的头文件

[^5]: 除<span><span>override</span></span>的<span><span>virtual</span></span>析构函数之外。

[^6]: 为了简化实现和举例，使用了<span><span>STL</span></span>中的<span><span>std::vector</span></span>。

[^7]: <span><span>class</span></span>的特性正好适合于将数据结构捧为神物的程序员，它们常常将数据结构置于类声明的最前面。

[^8]: 在<span><span><span>C</span></span></span>语言中，如果没有使用<span><span>typedef</span></span>，则定义一个结构体的指针，必须显式地加上<span><span>struct</span></span>关键字：<span><span>struct
    T\_Cell
    \*pcell</span></span>，而<span><span><span>C++</span></span></span>没有这方面的要求。

[^9]: 关于对称性，请参考<span><span>Kent
    Beck</span></span>的著作<span><span>《实现模式》</span></span>

[^10]: 例如社区中依然存在一批忠实的匈牙利的守护者，他们认为一个名称没有前缀和后缀标识它们的类型，他们几乎都看不懂代码了。

[^11]: 应该使用命名空间，避免增加模块前缀信息。

[^12]: 此处为了方便举例，使用了<span><span><span>C++</span></span></span><span><span>11</span></span>的<span><span>for-each,
    using</span></span>别名定义的语法，简化迭代器的操作。

[^13]: <span><span>Eclipse</span></span>默认使用蓝色与普通变量区别开来，其他<span><span>IDE</span></span>也提供类似的功能。

[^14]: 发布开源代码时，也常常需要增加必要的<span><span>GNU,
    BSD等</span></span>公共许可证

[^15]: 参考<span><span>Martin
    Flower</span></span>的著作《重构，改善既有代码的设计》

[^16]: 软件工程有一条黄金定律：任何问题都可以通过增加一个间接层来解决。
