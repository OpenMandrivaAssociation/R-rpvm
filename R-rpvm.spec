%global packname  rpvm
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.0.2
Release:          1
Summary:          R interface to PVM (Parallel Virtual Machine)
Group:            Sciences/Mathematics
License:          GPL version 2 or newer
URL:              None
Source0:          http://cran.r-project.org/src/contrib/Archive/rpvm/rpvm_1.0.2.tar.gz
Requires:         R-rsprng 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-rsprng 
BuildRequires:    libpvm-devel
Patch0:           rpvm_1.0.2-pvmgs.patch

%description
Provides interface to PVM APIs, and examples and documentation for its

%prep
%setup -q -c -n %{packname}
%patch0 -p1
(cd rpvm; autoreconf)

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/pvm*
%{rlibdir}/%{packname}/sla*
