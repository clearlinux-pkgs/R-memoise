#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-memoise
Version  : 1.0.0
Release  : 18
URL      : http://cran.r-project.org/src/contrib/memoise_1.0.0.tar.gz
Source0  : http://cran.r-project.org/src/contrib/memoise_1.0.0.tar.gz
Summary  : Memoisation of Functions
Group    : Development/Tools
License  : MIT
Requires: R-digest
Requires: R-testthat
BuildRequires : R-digest
BuildRequires : R-testthat
BuildRequires : clr-R-helpers

%description
# memoise [![Travis-CI Build Status](https://travis-ci.org/hadley/memoise.svg?branch=master)](https://travis-ci.org/hadley/memoise) [![Coverage Status](https://img.shields.io/codecov/c/github/hadley/memoise/master.svg)](https://codecov.io/github/hadley/memoise?branch=master)

%prep
%setup -q -c -n memoise

%build

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library memoise
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library memoise


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/memoise/DESCRIPTION
/usr/lib64/R/library/memoise/INDEX
/usr/lib64/R/library/memoise/LICENSE
/usr/lib64/R/library/memoise/Meta/Rd.rds
/usr/lib64/R/library/memoise/Meta/hsearch.rds
/usr/lib64/R/library/memoise/Meta/links.rds
/usr/lib64/R/library/memoise/Meta/nsInfo.rds
/usr/lib64/R/library/memoise/Meta/package.rds
/usr/lib64/R/library/memoise/NAMESPACE
/usr/lib64/R/library/memoise/NEWS.md
/usr/lib64/R/library/memoise/R/memoise
/usr/lib64/R/library/memoise/R/memoise.rdb
/usr/lib64/R/library/memoise/R/memoise.rdx
/usr/lib64/R/library/memoise/help/AnIndex
/usr/lib64/R/library/memoise/help/aliases.rds
/usr/lib64/R/library/memoise/help/memoise.rdb
/usr/lib64/R/library/memoise/help/memoise.rdx
/usr/lib64/R/library/memoise/help/paths.rds
/usr/lib64/R/library/memoise/html/00Index.html
/usr/lib64/R/library/memoise/html/R.css
