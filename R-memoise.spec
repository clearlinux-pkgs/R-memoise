#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-memoise
Version  : 0.2.1
Release  : 14
URL      : http://cran.r-project.org/src/contrib/memoise_0.2.1.tar.gz
Source0  : http://cran.r-project.org/src/contrib/memoise_0.2.1.tar.gz
Summary  : Memoise functions
Group    : Development/Tools
License  : MIT
Requires: R-digest
BuildRequires : R-digest
BuildRequires : clr-R-helpers

%description
# memoise
If a function is called multiple times with the same input, you can
often speed things up by keeping a cache of known answers that it can
retrieve. This is called memoisation <http://en/wikipedia.org/wiki/Memoization>.
The `memoise` package provides a simple syntax

%prep
%setup -q -c -n memoise

%build

%install
rm -rf %{buildroot}
export LANG=C
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library memoise
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
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
/usr/lib64/R/library/memoise/NEWS
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
