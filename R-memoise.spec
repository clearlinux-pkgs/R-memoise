#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-memoise
Version  : 2.0.1
Release  : 102
URL      : https://cran.r-project.org/src/contrib/memoise_2.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/memoise_2.0.1.tar.gz
Summary  : 'Memoisation' of Functions
Group    : Development/Tools
License  : MIT
Requires: R-cachem
Requires: R-rlang
BuildRequires : R-cachem
BuildRequires : R-rlang
BuildRequires : buildreq-R

%description
call it again with the same arguments it returns the previously computed
    value.

%prep
%setup -q -c -n memoise
cd %{_builddir}/memoise

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641057340

%install
export SOURCE_DATE_EPOCH=1641057340
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library memoise
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library memoise
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library memoise
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc memoise || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/memoise/DESCRIPTION
/usr/lib64/R/library/memoise/INDEX
/usr/lib64/R/library/memoise/LICENSE
/usr/lib64/R/library/memoise/Meta/Rd.rds
/usr/lib64/R/library/memoise/Meta/features.rds
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
/usr/lib64/R/library/memoise/tests/testthat.R
/usr/lib64/R/library/memoise/tests/testthat/helper.R
/usr/lib64/R/library/memoise/tests/testthat/test-filesystem.R
/usr/lib64/R/library/memoise/tests/testthat/test-gcs.R
/usr/lib64/R/library/memoise/tests/testthat/test-memoise.R
/usr/lib64/R/library/memoise/tests/testthat/test-s3.R
